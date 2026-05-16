from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["bizlangai_db"]

# Create collections if they don't exist
if "knowledge_base" not in db.list_collection_names():
    db.create_collection("knowledge_base")
    print("Created knowledge_base collection")
else:
    print("knowledge_base collection already exists")

print("Database initialization complete.")
