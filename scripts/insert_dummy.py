from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["bizlangai_db"]
collection = db["knowledge_base"]

# Insert a dummy document
result = collection.insert_one({"dummy": True, "message": "This is to initialize the collection so it shows up in Atlas."})
print(f"Inserted dummy document with ID: {result.inserted_id}")

print("Initialization complete.")
