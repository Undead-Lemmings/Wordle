# Demo functionality

word = "LOLES"

guess = "LINLD"

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

for letter_index in range(len(guess)):
    if guess[letter_index] == word[letter_index]:
        print(f"[{guess[letter_index]}]", end="")
    elif guess[letter_index] in word:
        print(f"({guess[letter_index]})",end="")
    else:
        print("_",end="")


