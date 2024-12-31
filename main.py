# WORDLE!

# Just need choice to select the initial word

from random import choice

# Chooses the answer word
def select_word():
    wordlist = []
    with open("wordlist.txt", "r") as file:
        raw_words = file.readlines()
        for possible_word in raw_words:
            wordlist.append(possible_word.replace("\n", "",))
    return str(choice(wordlist).upper())

# Tracks number of guesses
def guess_no():
    pass

# Provides last guess results
def guess_results(guess,word):

    print("")




# shows available letters
def alphabet(remaining_letters):
    print(remaining_letters)

def main():
    gaming = True
    guess = ""
    remaining_letters = ["A","B","C","D","E","F","G","H","U","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    word = select_word()
    print(word)
    while gaming:
        guess = input("Please enter your word: ").upper
        if guess > word:
            print("You")



if __name__ == "__main__":
    main()