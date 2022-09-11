"""EX 03: Structured Wordle - Creating an actual workable Wordle!"""

__author__ = "730546880"


def contains_char(given_string: str, specified_character: str) -> bool:
    """Given the subjects as a parameter, returns a boolean value whether the string contains that specific character."""
    assert len(specified_character) == 1
    counter: int = 0
    while counter < len(given_string):
         if given_string[counter] == specified_character:
            return True
            counter += 1
         
    return False

WHITE_BOX: str = "\U00002B1C"  #  white box emoji if the letter is incorrect and the position is incorrect
GREEN_BOX: str = "\U0001F7E9"  #  yellow box emoji if the letter is correct but the position is incorrect
YELLOW_BOX: str = "\U0001F7E8" 

def emojified(guess: str, secret: str) -> str:
    """Print the colored emojis, depending on whether the letter is correct, or the position is correct."""
    assert len(guess) == len(secret)
    counter: int = 0
    emoji_string: str = ""
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            emoji_string += GREEN_BOX

        elif contains_char(guess, secret[counter]):
            emoji_string += YELLOW_BOX

        else:
            emoji_string += WHITE_BOX
        
        counter += 1
    
    return emoji_string

def input_guess(expected_length: int):
    """Prompts the user for the guess and continue prompting them until they provide a guess of the expected length. """
    
print(emojified("apple", "akhil"))


