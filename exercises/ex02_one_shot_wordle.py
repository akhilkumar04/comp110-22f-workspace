"""EX 02: One Shot Wordle - Only one chance to guess the word"""


__author__ = "730546880"

word: str = input("What is your 6-letter guess? ")
secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0

while len(word) != 6:
    word = input("That was not 6 letters! Try again: ")


if len(word) == 6:
    while index < len(secret_word):
        if word [index] == secret_word[index]:
            print(GREEN_BOX)


        else:
            search: bool = False
            alternate_index: int = 0
            while search != True and alternate_index < len(secret_word):
                if word[index] == secret_word[alternate_index]:
                    search = True
                else:
                    alternate_index = alternate_index + 1
            
            if search == True:
                print(YELLOW_BOX)
            else:
                print(WHITE_BOX)
                
        index = index + 1

if word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    
