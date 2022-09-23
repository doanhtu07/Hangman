from collections import defaultdict
import os
from random import randint
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

words = []
for bytes in WORDS:
    word = bytes.decode("utf-8")
    words.append(word)


def game(word: str, errors=3):
    curState = ["_" for _ in range(len(word))]

    charMap = defaultdict(list)
    for i in range(len(word)):
        charMap[word[i]].append(i)

    guessed = set()

    while errors > 0:
        print()

        if "_" not in curState:
            print(f"You won! The word is `{word}`.")
            print()
            return

        print("Current state: ", " ".join(curState))
        userInput = input(
            f"Guess a letter ({errors} chances left) (-e for exit, -c for clear screen, -r for reveal): ")

        if userInput == "-e":
            print()
            return

        if userInput == "-c":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if userInput == "-r":
            print()
            print(f"Give up already? The word is `{word}`.")
            print()
            return

        if not userInput.isalpha() or len(userInput) != 1:
            print("Invalid input! Must be alphabetic and length = 1.")
            continue

        if userInput in guessed:
            print("You already guessed this letter.")
            continue

        guessed.add(userInput)

        if userInput not in charMap:
            errors -= 1

        else:
            for index in charMap[userInput]:
                curState[index] = userInput

    print()
    print(f"You did not make it. The word is `{word}`. Good luck next time!")
    print()


difficulty = input(
    "Choose difficulty (Easy | Medium | Hard, Default is Hard): ")
randomWord = words[randint(0, len(words)-1)]

if difficulty == "Easy":
    game(randomWord, 10)
elif difficulty == "Medium":
    game(randomWord, 5)
else:
    game(randomWord)
