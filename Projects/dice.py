import random

roll_count = 0

while True:
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    roll_count += 1
    print(f"({die_1}, {die_2})")

    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        print(f"Thank you for playing.Your dice count is {roll_count}")
        break