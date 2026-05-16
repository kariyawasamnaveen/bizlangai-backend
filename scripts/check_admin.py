import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.crud import get_user_by_email
from app.utils.hash import verify_password

user = get_user_by_email("admin@bizlangai.com")
if user:
    print("User found!")
    print(f"Role: {user['role']}")
    print(f"Username: {user['username']}")
    print(f"Password Hash: {user['password']}")
    valid = verify_password("Admin@123", user["password"])
    print(f"Password is valid: {valid}")
else:
    print("User not found!")
