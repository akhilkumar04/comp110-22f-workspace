"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730546880"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Word must be 5 letters.")
    exit()

character: str = input("Enter a single character: ")

if len(character) > 1:
    print("Character must be a letter.")
    exit()

print("Searching for " + str(character) + " in " + str(word))
character_count: int = 0

if word[0] == character:
    print(str(character) + " is found at index 0.")
    character_count = character_count + 1

if word[1] == character:
    print(str(character) + " is found at index 1.")
    character_count = character_count + 1

if word[2] == character:
    print(str(character) + " is found at index 2.")
    character_count = character_count + 1

if word[3] == character:
    print(str(character) + " is found at index 3.")
    character_count = character_count + 1

if word[4] == character:
    print(str(character) + " is found at index 4.")
    character_count = character_count + 1

print(str(character_count) + " instances of " + str(character) + " were found in " + str(word))
