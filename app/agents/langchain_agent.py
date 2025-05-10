# app/agents/langchain_agent.py

from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import matplotlib.pyplot as plt
import os
from uuid import uuid4

def run_pandas_agent(prompt: str, df):
    print("📊 LangChain Agent received data:\n", df.head(10))

    # Ensure chart output folder exists
    os.makedirs("static/charts", exist_ok=True)

    try:
        # ✅ Create agent with output parsing recovery enabled
        agent = create_pandas_dataframe_agent(
            ChatOpenAI(model="gpt-4o", temperature=0),
            df,
            verbose=True,
            allow_dangerous_code=True,
            agent_executor_kwargs={
                "handle_parsing_errors": True  # ✅ Important fix
            }
        )

        # ✅ Detect chart-related prompts
        if any(keyword in prompt.lower() for keyword in ["chart", "plot", "graph", "bar", "pie", "line"]):
            print("📈 Chart request detected...")

            chart_id = str(uuid4())
            chart_path = f"static/charts/{chart_id}.png"

            try:
                # Example chart: Revenue by Region
                df.groupby("Region")["Revenue"].sum().plot(kind="bar", color="skyblue")
                plt.title("Revenue by Region")
                plt.ylabel("Revenue")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(chart_path)
                plt.close()

                return f"![Chart](/static/charts/{chart_id}.png)"
            except Exception as chart_error:
                print("❌ Chart generation error:", chart_error)
                return "⚠️ Failed to generate chart from data."

        # 🧠 Otherwise, return normal LLM response
        result = agent.invoke({"input": prompt})
        return result["output"]

    except Exception as e:
        print("❌ LangChain Agent error:", e)
        return f"LangChain Agent error: {str(e)}"
