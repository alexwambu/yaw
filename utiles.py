import os

def ensure_storage_dir():
    os.makedirs("storage", exist_ok=True)
