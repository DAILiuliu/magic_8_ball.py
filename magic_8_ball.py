import random

answers: list[str] = [
    "Yes, definitely.",
    "Most likely.",
    "Ask again later.",
    "Not this time.",
]

while True:
    question = input("Ask the Magic 8 Ball a question (or type 'quit' to exit): ")
    if question.lower() == "quit":
        break

    print("The Magic 8 Ball is thinking...")
    print(random.choice(answers))