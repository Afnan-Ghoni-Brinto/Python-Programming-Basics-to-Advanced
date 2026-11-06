"""Guess a random number from 1 to 100."""
import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess a number from 1 to 100. Enter q to quit.")
    while True:
        guess_text = input("Your guess: ").strip()
        if guess_text.lower() == "q":
            print("Game ended")
            break
        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number")
            continue
        if not 1 <= guess <= 100:
            print("Choose between 1 and 100")
            continue
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You used {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
