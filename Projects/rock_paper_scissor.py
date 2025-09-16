import random

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
user_win = 0
com_win = 0
tie = 0

while True:
    user_choice = input("Rock, paper or scissor? (r/p/s): ").lower()
    choices = ('r', 'p', 's')

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
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p') ):
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