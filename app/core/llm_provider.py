import os
import requests
import openai

# ✅ Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FLOWISE_API_URL = os.getenv("FLOWISE_API_URL")

# ✅ Print loaded values to confirm
print("🔥 FLOWISE_API_URL =", FLOWISE_API_URL)
print("🔥 OPENAI_API_KEY =", OPENAI_API_KEY[:5] + "..." if OPENAI_API_KEY else "❌ Not Loaded")

# ✅ Set OpenAI key
openai.api_key = OPENAI_API_KEY

def query_openai(prompt: str) -> str:
    """
    Send prompt to OpenAI GPT model and return the response.
    """
    try:
        print("📤 Prompt sent to OpenAI:", prompt)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" or "gpt-4o"
            messages=[
                {"role": "system", "content": "You are a helpful business assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        output = response.choices[0].message["content"]
        print("📥 OpenAI response:", output)
        return output

    except Exception as e:
        return f"❌ OpenAI Error: {str(e)}"

def query_flowise(prompt: str) -> str:
    """
    Send prompt to Flowise REST API and return the response.
    """
    try:
        print("📤 Prompt sent to Flowise:", prompt)

        response = requests.post(
            FLOWISE_API_URL,
            json={"question": prompt},
            timeout=10
        )

        print("📥 Flowise response:", response.text)

        if response.status_code == 200:
            return response.json().get("text", "⚠️ No response from Flowise")
        else:
            return f"⚠️ Flowise API Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"❌ Flowise Error: {str(e)}"
