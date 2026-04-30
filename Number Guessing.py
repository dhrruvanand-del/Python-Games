import random


def start_game():
    target = random.randint(1, 100)
    print("--- Number Guessing Game ---")

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == target:
                print("You won!")
                break
            elif guess < target:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    start_game()
