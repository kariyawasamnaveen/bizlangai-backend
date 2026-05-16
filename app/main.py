# app/main.py

import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles  # ✅ For serving chart images

# 🔥 Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=dotenv_path)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 📦 Import all endpoints (chat, auth, upload)
from app.api.endpoints import chat, auth, upload

# 🚀 Create FastAPI app instance
app = FastAPI()

# 🌐 CORS Configuration - Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Serve static chart images
app.mount("/static", StaticFiles(directory="static"), name="static")

# 🦠 Root endpoint to check API status
@app.get("/")
def root():
    return {"message": "BizLangAI API is running ✅"}

# 🔗 Register route groups
app.include_router(chat.router)
app.include_router(auth.router)
app.include_router(upload.router)
