# WORDLE!

# Just need choice to select the initial word

from random import choice


# my Dot made colours in her Wordle and by gosh do I want to do the same now >:[
def colourise(funguess):
    colourguess = []
    # ANSI Escape sequences seem to be the easiest (not involving additional libraries) way do this
    # colours needed 32 - green     = "\033[32mCorrectLetterCorrectPlace\033[0m"
    #                33 - Yellow    =  "\033[33mCorrectLetterWrongPlace\033[0m"
    # function strips brackets, adds colour, moves on with life idk
    for i in funguess:
        if "[" in i:
            i = i.replace("[", "")
            i = i.replace("]","")
            i = f"\033[32m{i}\033[0m"
            colourguess.append(i)   
        elif "(" in i:
            i = i.replace("(", "")
            i = i.replace(")", "")
            i = f"\033[33m{i}\033[0m"
            colourguess.append(i)
        else:
            colourguess.append(i)
    return " ".join(colourguess)



# Chooses the answer word
def select_word():
    wordlist = []
    with open("wordlist.txt", "r") as file:
        raw_words = file.readlines()
        for possible_word in raw_words:
            wordlist.append(possible_word.replace("\n", "",))
    return wordlist

# Tracks number of guesses
def guess_no(total_guesses, number):
    return total_guesses - number

def input_validation(guess):
    words = select_word()
    if guess.lower() in words:
        return True
    else:
        return False

# Checks for [Correct Letter/Correct Place] and (Correct Letter/Wrong Place) 
def guess_results(guess,word):
    status = ["_"] * len(word)
    for i in range(len(guess)):
        if guess[i] == word[i]:
            status[i] = f"[{guess[i]}]"
    for i in range(len(guess)):
        if status[i] != f"[{guess[i]}]" and guess[i] in word and word.count(guess[i]) > (status.count(f"[{guess[i]}]") + status.count(f"({guess[i]})")):
                status[i] = f"({guess[i]})"
    return status

# shows available letters
def alphabet(letters, guess, word):
    new_remaining_letters = []
    for i in letters:
        if i in guess:
            if i in word:
                new_remaining_letters.append(f"\033[32m{i}\033[0m")
            else:
                new_remaining_letters.append("_")
        else:
            new_remaining_letters.append(i)
    return new_remaining_letters

    
def main():
    gaming = True
    guess = ""
    remaining_letters = ["A","B","C","D","E","F","G","H","U","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    tguesses = 6
    nguesses = 0
    word = choice(select_word()).upper()
    print(word)
    while gaming:
        guess = input("Please enter your word: ").upper()
        if input_validation(guess):    
            nguesses += 1
            # Uses guess function to get letters as a list, transforms them into colours and returns string with colourise fun
            print(colourise(guess_results(guess, word)))
            # Update and print the remaining letters
            alphabet(remaining_letters, guess, word)
            remaining_letters = alphabet(remaining_letters, guess, word)
            print(" ".join(remaining_letters))
            # Response to guess correct/out of turns/next round
            if guess == word:
                print("*********************************************************")
                print("CONGRATULATIONS! YOU WIN WORDLE! YOU LITTLE WORDLER 😘😘")
                print("*********************************************************")
                gaming = False
            elif guess_no(tguesses, nguesses) == 0:
                print("*********************************************************")
                print(f"AW NO! YOU HAVE LOST THE WORDLE! THE CORRECT WORD WAS {word.upper()}")
                print("*********************************************************")
                gaming = False
            else:
                print(f"You have {guess_no(tguesses,nguesses)} guesses left!")
        else:
            print("SO SORRY! THAT WORD IS NOT ON OUR LIST BUT WE ARE CERTAIN IT WAS AN EXCELLENT WORD!")

if __name__ == "__main__":
    main()