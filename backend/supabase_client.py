import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import Client, create_client


def get_supabase_client() -> Client:
    """Create and return a Supabase client using environment variables."""
    # Look for a .env file in the project root and the backend folder.
    base_dir = Path(__file__).resolve().parent
    env_paths = [base_dir / ".env", base_dir.parent / ".env"]

    for env_path in env_paths:
        if env_path.exists():
            load_dotenv(env_path)

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url or not supabase_key:
        raise ValueError(
            "Missing Supabase credentials. Please set SUPABASE_URL and SUPABASE_KEY in your .env file."
        )

    return create_client(supabase_url, supabase_key)
