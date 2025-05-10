# app/utils/jwt_handler.py

from jose import jwt
import datetime

SECRET_KEY = "your-secret"  # ⬅️ Use same key as in .env

def create_access_token(user_id: str, role: str):
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
