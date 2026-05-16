# app/db/redis_client.py
import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

try:
    redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    # Ping to check connection
    redis_client.ping()
    print("✅ Connected to Redis")
except Exception as e:
    print(f"⚠️ Could not connect to Redis: {e}")
    redis_client = None
