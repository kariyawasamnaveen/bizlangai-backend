# app/db/database.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Initialize client without immediate connection check to avoid import timeouts
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["bizlangai_db"]

# Collections
users_collection = db["users"]
chats_collection = db["chats"]
