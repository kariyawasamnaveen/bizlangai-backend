# app/services/upload_service.py

import pandas as pd
import json
import os

UPLOAD_DIR = "uploads"
LAST_UPLOAD_PATH = "last_upload.json"


def save_uploaded_file(file_path: str) -> list:
    """
    Reads the uploaded CSV/Excel file and saves data to last_upload.json.
    Returns the full data as a list of dicts.
    """
    try:
        # Read CSV or Excel
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")

        # Convert to list of dicts
        data = df.to_dict(orient="records")
        print(f"✅ Uploaded rows: {len(data)}")

        # Save to JSON
        with open(LAST_UPLOAD_PATH, "w") as f:
            json.dump(data, f)

        return data

    except Exception as e:
        print("❌ Error saving uploaded file:", e)
        return []


def get_last_uploaded_data() -> list:
    """
    Reads the most recently uploaded file from last_upload.json.
    Returns a list of dict rows.
    """
    try:
        with open(LAST_UPLOAD_PATH, "r") as f:
            data = json.load(f)
        print(f"📄 Loaded {len(data)} rows from last_upload.json")
        return data
    except Exception as e:
        print("⚠️ Could not load uploaded file:", e)
        return []
