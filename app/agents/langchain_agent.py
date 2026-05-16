# app/agents/langchain_agent.py
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

import matplotlib.pyplot as plt
import os
from uuid import uuid4
from app.services.knowledge_service import knowledge_service

def run_pandas_agent(prompt: str, df):
    print("📊 LangChain Agent received data:\n", df.head(10))
    os.makedirs("static/charts", exist_ok=True)

    try:
        agent = create_pandas_dataframe_agent(
            ChatOpenAI(model="gpt-4o", temperature=0),
            df,
            verbose=True,
            allow_dangerous_code=True,
            agent_executor_kwargs={"handle_parsing_errors": True}
        )

        if any(keyword in prompt.lower() for keyword in ["chart", "plot", "graph", "bar", "pie", "line"]):
            chart_id = str(uuid4())
            chart_path = f"static/charts/{chart_id}.png"
            try:
                # Basic chart logic (can be expanded)
                df.plot(kind="bar")
                plt.tight_layout()
                plt.savefig(chart_path)
                plt.close()
                return f"![Chart](/static/charts/{chart_id}.png)"
            except Exception as chart_error:
                return "⚠️ Failed to generate chart."

        result = agent.invoke({"input": prompt})
        return result["output"]
    except Exception as e:
        return f"Pandas Agent error: {str(e)}"

def run_knowledge_agent(prompt: str):
    """Retrieves information from the vector knowledge base."""
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.output_parsers import StrOutputParser

    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    retriever = knowledge_service.get_retriever()
    
    prompt_template = PromptTemplate.from_template(
        "Use the following pieces of retrieved context to answer the question. If you don't know the answer, say that you couldn't find any relevant information.\n\nContext: {context}\n\nQuestion: {question}"
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    qa_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )
    
    try:
        result = qa_chain.invoke(prompt)
        return result
    except Exception as e:
        print("❌ Knowledge Agent error:", e)
        return "⚠️ I couldn't find any relevant information in the uploaded documents."
