# Simple Quiz Engine

def display_question(q):
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)


def validate_answer(answer, options):
    valid = ["a", "b", "c", "d"]
    if answer.lower() in valid:
        return True
    return False


def check_answer(answer, correct):
    if answer.lower() == correct.lower():
        return True
    return False


def update_score(score, is_correct):
    if is_correct:
        score = score + 1
    return score


def display_results(score, total):
    percentage = (score / total) * 100
    incorrect = total - score

    print("\n----- Final Results -----")
    print("Correct answers   :", score)
    print("Incorrect answers :", incorrect)
    print("Score             :", score, "/", total)
    print("Percentage        :", percentage, "%")

    if percentage >= 80:
        print("Result            : Excellent")
    elif percentage >= 60:
        print("Result            : Good")
    elif percentage >= 40:
        print("Result            : Fair")
    else:
        print("Result            : Needs Improvement")
    print("-------------------------")


# Questions
questions = [
    {
        "question": "1. What is the capital of Ethiopia?",
        "options": ["a) Nairobi", "b) Addis Ababa", "c) Cairo", "d) Lagos"],
        "answer": "b"
    },
    {
        "question": "2. How many continents are there?",
        "options": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "answer": "c"
    },
    {
        "question": "3. What is 5 + 7?",
        "options": ["a) 10", "b) 11", "c) 12", "d) 13"],
        "answer": "c"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "answer": "b"
    },
    {
        "question": "5. What is the largest ocean?",
        "options": ["a) Atlantic", "b) Indian", "c) Arctic", "d) Pacific"],
        "answer": "d"
    }
]


# Main quiz loop (can play again)
while True:
    score = 0
    total = len(questions)

    print("\n===== QUIZ START =====")

    for q in questions:
        display_question(q)

        answer = input("Your answer (a/b/c/d): ")

        # Keep asking until valid option is entered
        while not validate_answer(answer, q["options"]):
            print("Invalid option. Please enter a, b, c, or d.")
            answer = input("Your answer (a/b/c/d): ")

        is_correct = check_answer(answer, q["answer"])
        score = update_score(score, is_correct)

        if is_correct:
            print("Correct!")
        else:
            print("Wrong! Correct answer was:", q["answer"])

    display_results(score, total)

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break