from fastapi import APIRouter, Request, Depends
from app.services.chat_service import get_llm_response, save_chat
from app.api.deps import get_current_user

router = APIRouter(prefix="/api")

@router.post("/chat")
async def chat(request: Request, current_user: dict = Depends(get_current_user)):
    """
    Accepts a prompt and returns a response from selected LLM.
    Only allows users with role 'admin' or 'manager'.
    """
    body = await request.json()

    prompt = body.get("prompt")
    source = body.get("source", "openai")
    user_id = current_user.get("user_id", "anonymous")

    if not prompt:
        return {"error": "❌ Prompt is required"}

    if current_user.get("role") not in ["admin", "manager"]:
        return {"error": "🔒 Access denied. Only admin or manager can chat."}

    try:
        # ✅ FIX: Await the async function
        reply = await get_llm_response(prompt, source)

        # ✅ Now reply is a real string, safe to store
        save_chat(user_id, prompt, reply)

        return {"response": reply}

    except Exception as e:
        print("❌ Chat error:", e)
        return {"error": f"Internal Server Error: {str(e)}"}
