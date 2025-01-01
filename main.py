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
    status = []
    # Checks each letter of word with the corresponding letter of the guess
    for i in range(len(guess)):
        if status.count(f"[{guess[i]}]") + status.count(f"({guess[i]})") >= word.count(word[i]):
            status.append("_")
        elif guess[i] == word[i]:
            status.append(f"[{guess[i]}]")
        elif guess[i] in word:
            status.append(f"({guess[i]})")
        else:
            status.append("_")
    return status        
        


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
        guess = input("Please enter your word: ").upper()
        print(guess_results(guess, word))



if __name__ == "__main__":
    main()