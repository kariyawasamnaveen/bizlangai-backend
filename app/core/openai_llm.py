import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # from .env file or env variable

async def generate_response(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" or "gpt-4o"
            messages=[
                {"role": "system", "content": "You are a helpful business assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {str(e)}"
