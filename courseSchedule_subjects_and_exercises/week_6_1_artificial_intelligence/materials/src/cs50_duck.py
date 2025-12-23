import os
from dotenv import load_dotenv
from openai import OpenAI


def main():
    """Main function to run the CS50 Duck assistant."""

    # Load environment variables
    load_dotenv()

    # Initialize OpenAI client
    client = OpenAI(api_key=os.environ.get("API_KEY"))

    if not client.api_key:
        print("Error: API_KEY not found in .env file")
        return

    # System prompt - CS50 Duck personality
    system_prompt = os.environ.get(
        "SYSTEM_PROMPT",
        "You are a friendly and supportive teaching assistant for CS50. You are also a duck.",
    )

    print("=" * 50)
    print("🦆 CS50 Duck Teaching Assistant")
    print("=" * 50)
    print("Type 'quit', 'exit', or 'bye' to end the session.")
    print("-" * 50)

    while True:
        # Get user question
        user_prompt = input("\n🧑‍🎓 What's your question? ").strip()

        # Check for exit commands
        if user_prompt.lower() in ["quit", "exit", "bye", "q"]:
            print("\n🦆 Quack! Good luck with your studies!")
            break

        if not user_prompt:
            print("Please enter a question.")
            continue

        try:
            # Get AI response
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                model=os.environ.get("DEFAULT_MODEL", "gpt-4o"),
                max_tokens=int(os.environ.get("MAX_TOKENS", 1000)),
                temperature=float(os.environ.get("TEMPERATURE", 0.7)),
            )

            response_text = chat_completion.choices[0].message.content

            # Display response
            print("\n" + "=" * 50)
            print("🦆 CS50 Duck says:")
            print("-" * 50)
            print(response_text)
            print("=" * 50)

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please check your API key and internet connection.")


if __name__ == "__main__":
    main()
