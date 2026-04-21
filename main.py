from claude_model import ClaudeModel
from ollama_model import OllamaModel
from comparator import Comparator


TEST_PROMPTS = [
    "Explain recursion in one paragraph.",
    "Write a Python function that reverses a string.",
    "What is the difference between RAM and ROM?",
    "Explain what a neural network is in simple terms.",
]


def main():
    print("\n" + "="*60)
    print("     LLM COMPARISON LAB")
    print("="*60)
    print("Comparing Claude Haiku vs Llama 3.2 (local)\n")

    claude = ClaudeModel()
    llama = OllamaModel()
    comparator = Comparator(claude, llama)

    while True:
        print("\nWhat would you like to do?")
        print("1. Run all test prompts")
        print("2. Enter custom prompt")
        print("3. Quit")

        choice = input("\nEnter 1-3: ").strip()

        if choice == "1":
            for prompt in TEST_PROMPTS:
                comparator.compare(prompt)
                print("\n" + "-"*60)

        elif choice == "2":
            prompt = input("\nEnter your prompt: ").strip()
            if prompt:
                comparator.compare(prompt)

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Enter 1-3.")


if __name__ == "__main__":
    main()