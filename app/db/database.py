# database.py – MongoDB init
# Placeholder for DB connection
# app/db/database.py
from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["bizlangai_db"]

# Collections
users_collection = db["users"]
chats_collection = db["chats"]
