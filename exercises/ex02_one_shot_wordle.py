"""EX 02: One Shot Wordle - Only one chance to guess the word.""" #  description of the program


__author__ = "730546880"  #  PID number

guess: str = input("What is your 6-letter guess? ") 

#Asks the user to input a 6-letter word
secret_word: str = "python"  

#secret word they have to guess
WHITE_BOX: str = "\U00002B1C"  #  white box emoji if the letter is incorrect and the position is incorrect
GREEN_BOX: str = "\U0001F7E9"  #  yellow box emoji if the letter is correct but the position is incorrect
YELLOW_BOX: str = "\U0001F7E8"  #  green box emoji if the letter is correct and the position is correct
index: int = 0  #  counter variable to go throuhg each letter of the word
s: str = ""
while len(guess) != 6:  #  when the word isn't 6 letters
    guess = input(f'That was not {len(secret_word)} letters! Try again: ')  #  Error message indicated your word isn't characters


if len(guess) == 6:  #  when word is 6 letters
    while index < len(secret_word):  #  finite loop to go through one letter at a time to finding matching letters and positions
        if guess[index] == secret_word[index]:  #  if the secret word matches the letter and position
            s = s + GREEN_BOX #  string concantenation for green box emoji
        else:
            position_search: bool = False  #  searching for letters in incorrect positions is turned off
            alternate_index: int = 0  #  using an alternate index to not confuse the variables
            while position_search is not True and alternate_index < len(secret_word):  #  finite loop to go thorugh one letter at a time to find matching letters
                if guess[index] == secret_word[alternate_index]:  #  if the secret word has the correct letters in theiur incorrect positions
                    position_search = True  #  letter was found in incorrect position is turned on
                else:
                    alternate_index = alternate_index + 1  #  increments the alternate index variable by 1
            if position_search is True:  #  output when search is True
                s = s + YELLOW_BOX #  string concantenation for yellow box emoji
            else:
               s = s + WHITE_BOX  #  string concantenation for white box emoji
        index = index + 1  #  increments the index variable by 1

print(s)
if guess == secret_word:  #  if the guess was correct
    print("Woo! You got it!")  #  prints this statement indicated your guess was right
else:
    print("Not quite. Play again soon!")  #  prints this statement indicating your guess was incorrect
    
