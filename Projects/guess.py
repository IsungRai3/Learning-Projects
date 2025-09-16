import random
print("""
------------GUESS THE NUMBER-----------
YOU'VE GOT 5 CHANCE TO GUESS THE CORRECT NUMBER!!!
""")
guess_counter = 0
max_guess = 5
while True:
    try:
        limit = int(input("Set your limit: "))
        if limit < 0:
            print("Choose the number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid input!! Please enter a number.")

random_number = random.randint(1, limit)


while guess_counter < max_guess:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        break

    guess_counter += 1

    if random_number > guess:
        print("Too low! Try again! Guess left: ",max_guess - guess_counter)
    elif random_number < guess:
        print("Too high! Try again! Guess left: ",max_guess - guess_counter)
    else:
        print("Congratulation!!!")
        break
else:
    print(f"Out of guesses! The number was: {random_number}")