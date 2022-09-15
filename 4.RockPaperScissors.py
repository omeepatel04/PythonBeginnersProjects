import random

def play():
    user = input("Type 'S' for Scissors, 'R' for Rock or 'P' for Paper: ").lower()
    computer = random.choice(['s', 'r', 'p'])
    if computer == "s":
        print(f"Computer chose Sciccors")
    elif computer == "r":
            print(f"Computer chose Rock")
    else:
        print(f"Computer chose Paper")


    if user == 's' and computer == 'p' or user == 'r' and computer == 's' or user == 'p' \
        and computer == 'r':
        print("You Won!")
    elif computer == user:
        print("It's a Tie!")
    else:
        print("You Lost!")
 
play()