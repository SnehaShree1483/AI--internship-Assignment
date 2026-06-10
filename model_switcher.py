from google import genai

API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

MODELS = [
    "gemini-2.0-flash",
    "gemini-2.5-flash"
]

SYSTEM_PROMPT = "You are a helpful assistant. Keep your answer under 5 sentences."


def ask_model(model, question):

    prompt = f"""
{SYSTEM_PROMPT}

User Question:
{question}
"""

    try:

        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        print(response.text)
        print()

    except Exception as e:

        print(f"[Model Error: {e}]")
        print()


def main():

    print("=== Gemini Model Switcher ===")
    print(f"Models: {', '.join(MODELS)}")
    print("Type a question. Type 'quit' to exit.\n")

    while True:

        question = input("Your question: ").strip()

        if not question:
            continue

        if question.lower() == "quit":
            print("Bye!")
            break

        print()

        for model in MODELS:

            print(f"----- {model} -----\n")

            ask_model(model, question)

        again = input("Ask another question? (y/n): ").strip().lower()

        if again != "y":
            print("Bye!")
            break

        print()


if __name__ == "__main__":
    main()
