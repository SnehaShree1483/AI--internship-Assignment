from google import genai

# Paste your Gemini API key here
API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.0-flash"

SYSTEM_PROMPT = """
You are a debate coach.

When given a topic and a side, generate exactly 3 strong arguments.

Format your response exactly like this:

ARGUMENT 1: [title]
[2-3 sentence explanation with a real-world example]

ARGUMENT 2: [title]
[2-3 sentence explanation with a real-world example]

ARGUMENT 3: [title]
[2-3 sentence explanation with a real-world example]

Be persuasive, logical, and always use real-world examples.
"""


def get_side_choice():

    print("\nPick a Side for Debate:")
    print("1. FOR")
    print("2. AGAINST")

    while True:

        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            return "FOR"

        elif choice == "2":
            return "AGAINST"

        else:
            print("Invalid Choice. Enter 1 or 2.")


def generate_arguments(topic, side):

    prompt = f"""
Topic: {topic}

Side: {side}

Generate exactly 3 strong debate arguments.
"""

    print(f"\n---- Arguments {side}: '{topic}' ----\n")

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=f"{SYSTEM_PROMPT}\n\n{prompt}"
        )

        print(response.text)

    except Exception as e:

        print("Error:", e)
        print("Please try again later.")


def main():

    print("=== Debate Argument Generator ===")
    print("Type a topic. Type 'quit' to exit.\n")

    while True:

        user_input = input("Topic: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Bye, Let's catch up later.")
            break

        side = get_side_choice()

        generate_arguments(user_input, side)

        again = input("\nTry another topic? (y/n): ").strip().lower()

        if again != "y":
            print("Take Care, Have a great day.")
            break

        print()


if __name__ == "__main__":
    main()
