# Wordle!

## Gameplay:

Worlde is a game of word guessing. Each round begins with a 5-letter word being selected at random from a pre-defined list. You, the mighty player of the Wordle, will be presented with 5 spaces:

 <!--language: lang-none -->
    _ _ _ _ _
They are prompted to guess a word, after which, the word is return with a green letter (represented with a [ ]) in the correct place, and a yellow character (represented using ( )) if in the wrong place. In the below example, a player chooses "PLEAT" as their starting word. 


The returning response is:

<!-- language: lang-none -->
    [P] _ (E) (A) _

To keep things easy to track, the list of available letters is also returned, with the incorrect ones removed:
<!-- language: lang-none -->
    A B C D E F G H I J K _ M N O P Q R S _ U V W X Y Z

A full game should look like this:
<!-- language: lang-none -->
     _ _ _ _ _
    > Please provide a word: Pleat
     [P] _ (E) (A) _
     A B C D E F G H I J K _ M N O P Q R S _ U V W X Y Z
    > Please provide a word: pages
     [P] [A] _ [E] _
     A B C D E F _ H I J K _ M N O P Q R _ _ U V W X Y Z
    > Please provide a word: PACED
    [P] [A] [C] [E] [D]
    ********************************
    CONGRATULATIONS! YOU WIN WORDLE!
    ********************************

You will have a limit of 5 guesses. Good luck!

## Coding goals
Wordle obviously already [exists](https://www.nytimes.com/games/wordle/index.html). There are a few goals with this game:

1. Primarly I am wanting to famliarise myself with Python
2. Getting familiar with GITHUB as a platform is also good
3. Idk just having fun really

## Outstanding Game Goals
1. Replayability - New game (y/n) option after winning/losing
2. Better wordlist. Current one is a bit rubbish
3. Package into app using something like pyinstaller

## Special Mentions
 - To my Doteroo, like may she sparkle
 - To Tabatkins. I spent too long trying to regex a wordlist out of word dumps and they have just got the wordlist [here](https://github.com/tabatkins/wordle-list)