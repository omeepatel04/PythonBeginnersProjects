import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess > random_number:
            print("Guess Lower")
        elif guess < random_number:
            print("Guess Higher")

    print("Great! You guessed correctly")

guess(10)





