from typing import Any, Dict, List, Optional

from supabase_client import get_supabase_client


def save_conversation(
    user_id: str,
    user_message: str,
    ai_response: str,
    status: str = "AI_MODE",
    language: str = "uz",
) -> Dict[str, Any]:
    """Insert a new conversation into the Supabase conversations table."""
    client = get_supabase_client()
    data = {
        "user_id": user_id,
        "user_message": user_message,
        "ai_response": ai_response,
        "status": status,
        "language": language,
    }
    response = client.table("conversations").insert(data).execute()
    return response.data[0]


def get_history(user_id: str) -> List[Dict[str, Any]]:
    """Return all conversations for one user."""
    client = get_supabase_client()
    response = (
        client.table("conversations")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return response.data


def update_status(user_id: str, new_status: str) -> Optional[Dict[str, Any]]:
    """Update the latest conversation status for one user."""
    client = get_supabase_client()
    response = (
        client.table("conversations")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    conversation_id = response.data[0]["id"]
    update_response = (
        client.table("conversations")
        .update({"status": new_status})
        .eq("id", conversation_id)
        .execute()
    )
    return update_response.data[0]


def get_open_tickets() -> List[Dict[str, Any]]:
    """Return conversations that are not resolved yet."""
    client = get_supabase_client()
    response = (
        client.table("conversations")
        .select("*")
        .neq("status", "RESOLVED")
        .order("created_at", desc=True)
        .execute()
    )
    return response.data


def get_all_conversations() -> List[Dict[str, Any]]:
    """Return every conversation in the table."""
    client = get_supabase_client()
    response = (
        client.table("conversations")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return response.data
