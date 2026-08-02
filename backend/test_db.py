from crud import get_history, save_conversation


def main() -> None:
    """Insert and read back one sample conversation from Supabase."""
    saved = save_conversation(
        user_id="user_001",
        user_message="Hello, I need help with my order.",
        ai_response="I can help you with that.",
        status="AI_MODE",
        language="uz",
    )

    print("Saved conversation:")
    print(saved)

    history = get_history("user_001")

    print("\nConversation history:")
    for item in history:
        print(item)


if __name__ == "__main__":
    main()
