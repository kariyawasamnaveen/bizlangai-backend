import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils.hash import hash_password
from app.db.crud import create_user, get_user_by_email

def create_admin():
    email = "admin@bizlangai.com"
    if get_user_by_email(email):
        print("Admin user already exists.")
        return

    hashed = hash_password("Admin@123")
    create_user("System Admin", email, hashed, "admin")
    print("✅ Admin user created successfully.")

if __name__ == "__main__":
    create_admin()
