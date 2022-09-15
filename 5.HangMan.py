import random
import string 
from Extra import lives_visual
from Extra import words 

def get_valid_words(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_words(words)
    wordletters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedletters = set()

    lives = 6 

    while len(wordletters) > 0 and lives > 0:
        userletter = input("\nGuess a letter: ").upper()
        if userletter in alphabet - usedletters:
            usedletters.add(userletter)
            if userletter in wordletters:
                wordletters.remove(userletter)
            else:
                lives -= 1

        elif userletter in usedletters:
            print("You have already guessed that letter! ")

        else:
            print("Invalid Letter!")

        print(f"\nYou have {lives} lives left and you have guessed these letters: ", " ".join(usedletters))
        wordlist = [letter if letter in usedletters else "_" for letter in word]
        print(lives_visual[lives])
        print("Current word: ", " ".join(wordlist))

    if lives == 0:
        print(f"You Died! The word was {word}")
        print(lives_visual[lives])
    else:
        print(f"You guessed the word {word} correctly")

hangman()
