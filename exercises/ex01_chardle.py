"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730546880"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print(" Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + str(character) + " in " + str(word))
character_count: int = 0

if word[0] == character:
    print(str(character) + " found at index 0.")
    character_count = character_count + 1

if word[1] == character:
    print(str(character) + " found at index 1.")
    character_count = character_count + 1

if word[2] == character:
    print(str(character) + " found at index 2.")
    character_count = character_count + 1

if word[3] == character:
    print(str(character) + " found at index 3.")
    character_count = character_count + 1

if word[4] == character:
    print(str(character) + " found at index 4.")
    character_count = character_count + 1

if character_count == 0:
    print("No instances of " + str(character) + " found in " + str(word))

if character_count == 1:
    print("1 instance of " + str(character) + " found in " + str(word))

if character_count > 1:
    print(str(character_count) + " instances of " + str(character) + " found in " + str(word))
