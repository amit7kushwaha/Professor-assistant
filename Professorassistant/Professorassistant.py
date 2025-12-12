import random
from typing import List, Tuple, Optional


def load_question_bank(path: str) -> Optional[List[Tuple[str, str]]]:
    """
    Reads a question bank file and returns a list of (question, answer) tuples.
    Each question and its answer should be on consecutive lines.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        if len(lines) < 2:
            print("The file does not contain enough lines for question–answer pairs.")
            return None

        pairs = []
        for i in range(0, len(lines) - 1, 2):
            question = lines[i]
            answer = lines[i + 1]
            pairs.append((question, answer))

        return pairs

    except FileNotFoundError:
        print("❌ Error: The file path you provided does not exist.")
        return None


def create_exam(qa_pairs: List[Tuple[str, str]], num_questions: int, output_path: str):
    """
    Randomly selects unique question–answer pairs and writes them to the output file.
    """
    selected_pairs = random.sample(qa_pairs, num_questions)

    with open(output_path, "w", encoding="utf-8") as file:
        for question, answer in selected_pairs:
            file.write(question + "\n")
            file.write(answer + "\n\n")


def get_int(prompt: str) -> int:
    """Safely get an integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")


def main():
    print("Welcome to Professor Assistant 2.0.")
    name = input("Please enter your name: ").strip()
    print(f"Hello Professor {name}. I am here to help you create exams from a question bank.\n")

    while True:
        choice = input("Create an exam? (Yes | No): ").strip().lower()

        if choice == "no":
            print(f"Thank you, Professor {name}. Have a wonderful day!")
            break

        elif choice == "yes":
            path = input("Enter the path to the question bank file: ").strip()
            qa_pairs = load_question_bank(path)

            if not qa_pairs:
                continue  # try again

            print("✔ Question bank successfully loaded.")

            num_available = len(qa_pairs)
            print(f"There are {num_available} question–answer pairs available.")

            # Get number of questions
            num_questions = get_int("How many Q/A pairs do you want in the exam? ")

            if num_questions > num_available:
                print(f"❌ You requested {num_questions} questions, but only {num_available} are available.")
                print("Please try again.\n")
                continue

            output_path = input("Where should I save the exam file? ").strip()
            create_exam(qa_pairs, num_questions, output_path)

            print(f"🎉 Exam created successfully! Saved to: {output_path}\n")

        else:
            print("Please enter 'Yes' or 'No'.\n")


if __name__ == "__main__":
    main()
