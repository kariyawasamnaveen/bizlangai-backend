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
    
    chart_id = str(uuid4())
    chart_path = f"static/charts/{chart_id}.png"

    # Inject instructions to allow the agent to generate the chart dynamically
    custom_prompt = (
        f"{prompt}\n\n"
        f"IMPORTANT INSTRUCTION: If the user asks for a chart, plot, or graph, you MUST generate the Python code to draw it using matplotlib or seaborn based on the data. "
        f"You MUST save the generated figure EXACTLY to this file path: '{chart_path}'. "
        f"Do NOT use plt.show(). ALWAYS use plt.tight_layout() before saving. "
        f"After successfully saving the chart, your final output MUST include exactly this markdown string: ![Chart](/{chart_path})"
    )

    try:
        agent = create_pandas_dataframe_agent(
            ChatOpenAI(model="gpt-4o", temperature=0),
            df,
            verbose=True,
            allow_dangerous_code=True,
            agent_type="tool-calling"
        )

        result = agent.invoke({"input": custom_prompt})
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
        "You are a highly intelligent business AI assistant for BizLangAI. Use the following extracted context from the uploaded documents to answer the user's question. If the context is empty or doesn't have the exact answer, answer the best you can and gently mention if the PDF didn't contain that specific detail.\n\nContext: {context}\n\nQuestion: {question}"
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
