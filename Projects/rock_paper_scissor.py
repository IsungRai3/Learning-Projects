import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {ROCK: '🪨', PAPER: '📃', SCISSOR: '✂️'}
user_win = 0
com_win = 0
tie = 0

while True:
    user_choice = input("Rock, paper or scissor? (r/p/s): ").lower()
    choices = tuple(emojis.keys())

    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
        tie += 1
    elif (
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSOR and computer_choice == PAPER) ):
        print("You Win!")
        user_win += 1
    else:
        print("You lose!")
        com_win += 1

    again = input("Continue? (y/n):").lower()
    if again != 'y':
        print("Here are the final score:- ")
        print(f"""
Your score: {user_win}
Computer score: {com_win}
Tied: {tie}
""")
        break