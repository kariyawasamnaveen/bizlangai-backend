# app/services/chat_service.py

from app.core.openai_llm import generate_response  # async OpenAI handler
from app.core.llm_provider import query_flowise    # Flowise REST fallback
from app.db.database import chats_collection
from app.services.upload_service import get_last_uploaded_data
from app.agents.langchain_agent import run_pandas_agent, run_knowledge_agent  # ✅ LangChain Agents
import pandas as pd


async def get_llm_response(prompt: str, source: str = "openai") -> str:
    """
    Generate a response using the selected LLM source (OpenAI, Flowise, or LangChain),
    intelligently combining it with uploaded CSV/Excel content.
    """

    try:
        uploaded_data = get_last_uploaded_data()
    except Exception as e:
        print("⚠️ Error reading uploaded data:", e)
        uploaded_data = []

    print("📊 Total uploaded rows:", len(uploaded_data))

    # ✅ 1. Try Spreadsheet Analysis (Pandas Agent)
    if uploaded_data:
        try:
            print("🧠 Switching to LangChain PandasAgent...")
            df = pd.DataFrame(uploaded_data)
            return run_pandas_agent(prompt, df)
        except Exception as e:
            print("❌ LangChain Agent error:", e)

    # ✅ 2. Try Knowledge Base (RAG)
    try:
        print("🔍 Searching Knowledge Base...")
        response = run_knowledge_agent(prompt)
        if "I couldn't find any relevant information" not in response:
            return response
    except Exception as e:
        print("⚠️ Knowledge retrieval failed:", e)

    # 🧠 If no uploaded data or LangChain fails, enrich prompt manually
    if uploaded_data:
        try:
            headers = " | ".join(uploaded_data[0].keys())
            formatted_rows = "\n".join([
                " | ".join(str(row.get(col, "")) for col in uploaded_data[0].keys())
                for row in uploaded_data[:20]
            ])
            prompt = (
                f"You are an intelligent business data analyst.\n"
                f"Analyze the following uploaded sales data:\n\n"
                f"{headers}\n"
                f"{formatted_rows}\n\n"
                f"Now, based on the above data, answer this question:\n"
                f"{prompt}\n"
                f"If the question is ambiguous or unclear, explain what is missing."
            )
        except Exception as e:
            print("⚠️ Prompt enrichment failed:", e)

    # ✅ Call Flowise or OpenAI
    if source == "flowise":
        try:
            return query_flowise(prompt)
        except Exception as e:
            print("⚠️ Flowise error:", e)
            return f"Flowise error: {str(e)}"

    try:
        return await generate_response(prompt)
    except Exception as e:
        print("⚠️ OpenAI error:", e)
        return f"OpenAI error: {str(e)}"


def save_chat(user_id: str, prompt: str, response: str) -> None:
    """
    Save chat history to MongoDB.
    """
    try:
        chats_collection.insert_one({
            "user_id": user_id,
            "prompt": prompt,
            "response": response
        })
    except Exception as e:
        print("❌ Chat save error:", e)
