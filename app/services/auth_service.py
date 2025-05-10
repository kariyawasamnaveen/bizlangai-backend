# auth_service.py – Auth business logic
# Placeholder for login/signup logic
from jose import jwt

def create_jwt_token(user_id: str, role: str):
    payload = {
        "user_id": user_id,
        "role": role
    }
    token = jwt.encode(payload, "your-secret", algorithm="HS256")
    return token
