# Demo functionality
import random

# Get the words as an array

wordlist = []



with open("wordlist.txt", "r") as file:
    raw_words = file.readlines()
    for possible_word in raw_words:
        wordlist.append(possible_word.replace("\n", "",))

print(wordlist)

word = random.choice(wordlist).upper()
print(word)

# FFS I am a moron. I can just get the index of word using guess. Input verification can happen before doing this
""" 
for word_letters in range(len(word)):
    word_letter = word[word_letters]
    for guess_letters in range(len(guess)):
        guess_letter = guess[guess_letters]
        print(f"{word_letter}   {guess_letter}")
        if guess_letter == word_letter:
            print("Is in the correct place!")
"""
guess = input("Please enter a five letter word: ").upper()

for letter_index in range(len(guess)):
    if guess[letter_index] == word[letter_index]:
        print(f"[{guess[letter_index]}]", end="")
    elif guess[letter_index] in word:
        print(f"({guess[letter_index]})",end="")
    else:
        print("_",end="")


