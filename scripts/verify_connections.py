# scripts/verify_connections.py
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import client
from app.db.redis_client import redis_client

def test_mongodb():
    print("Testing MongoDB Connection...")
    try:
        if client:
            client.server_info()
            print("✅ MongoDB Connection Successful!")
        else:
            print("❌ MongoDB client is None (check MONGO_URI)")
    except Exception as e:
        print(f"❌ MongoDB Connection Failed: {e}")

def test_redis():
    print("\nTesting Redis Connection...")
    try:
        if redis_client:
            redis_client.ping()
            print("✅ Redis Connection Successful!")
        else:
            print("❌ Redis client is None (check REDIS_URL)")
    except Exception as e:
        print(f"❌ Redis Connection Failed: {e}")

if __name__ == "__main__":
    test_mongodb()
    test_redis()
