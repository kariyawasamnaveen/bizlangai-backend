# app/db/crud.py
from app.db.database import users_collection

def create_user(username, email, hashed_password, role="viewer"):
    return users_collection.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password,
        "role": role
    })

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})
