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
def guess_no(total_guesses, number):
    return total_guesses - number

# Provides last guess results
def guess_results(guess,word):
    status = ["_"] * len(word)
        # for loop  - makes sure correct letter/correct place is returned with []
    for i in range(len(guess)):
        if guess[i] == word[i]:
            status[i] = f"[{guess[i]}]"
    # for loop  - checks for correct letter/wrong plcae () and that the number of occurences in guess is less than the occurences in status
    for i in range(len(guess)):
        if status[i] != f"[{guess[i]}]" and guess[i] in word and word.count(guess[i]) > (status.count(f"[{guess[i]}]") + status.count(f"({guess[i]})")):
                status[i] = f"({guess[i]})"
    # makes sure the _ replaces any wrong letters
    for i in range(len(guess)):
        if guess[i] not in word:
            status[i] = "_"
    return status

def check_answer():
    pass


# shows available letters
def alphabet(remaining_letters):
    print(remaining_letters)

def main():
    gaming = True
    guess = ""
    difficulty = 6
    nguesses = 0
    remaining_letters = ["A","B","C","D","E","F","G","H","U","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    word = select_word()
    print(word)
    while gaming:
        nguesses += 1
        print(" ".join(guess_results(guess, word)))
        print(f"You have {guess_no(difficulty,nguesses)} guesses left!")
        guess = input("Please enter your word: ").upper()
        if "".join(guess_results(guess, word)).replace("[","").replace("]","") == word:
            print("*********************************************************")
            print("CONGRATULATIONS! YOU WIN WORDLE! YOU LITTLE WORDLER 😘😘")
            print("*********************************************************")
            gaming = False
        

if __name__ == "__main__":
    main()