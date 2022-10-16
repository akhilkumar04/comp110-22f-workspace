"""EX 03: Structured Wordle - Creating an actual workable Wordle!"""

__author__ = "730546880"

# The contains_char function will returns True if the given word meets the specified character
# and False if it doesn't.


def contains_char(given_string: str, specified_character: str) -> bool:
    """Given the subjects as a parameter, returns a boolean value whether the string contains that specific character."""
    assert len(specified_character) == 1
    counter: int = 0
    while counter < len(given_string):
        if given_string[counter] == specified_character:
            return True
        counter += 1
         
    return False


WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# The emojified function will print the emojis based on the letter and position of the letter.


def emojified(guess: str, secret: str) -> str:
    """Print the colored emojis, depending on whether the letter is correct, or the position is correct."""
    assert len(guess) == len(secret)
    counter: int = 0
    emoji_string: str = ""
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            emoji_string += GREEN_BOX

        elif contains_char(secret, guess[counter]):
            emoji_string += YELLOW_BOX

        else:
            emoji_string += WHITE_BOX
        
        counter += 1
    
    return emoji_string

# The input_guess asks the user to guess a word based on the length of the word. 


def input_guess(expected_length: int) -> str:
    """Prompts the user for the guess and continue prompting them until they provide a guess of the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f'That was not {expected_length} letters! Try again: ') 
        
    return guess
    
# The main function is the algorithm used to run the Wordle. 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    is_guess_correct: bool = False
    secret: str = "codes"
    while is_guess_correct is not True and turns <= 6:
        print(f"== Turn {turns}/6 ==")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            is_guess_correct = True
            print(f"You won in {turns}/6 turns!")
        else:
            turns += 1
    if is_guess_correct is not True:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()