"""EX06: Choose Your Own Adventure - UNC Trivia Game!"""
__author__ = "730546880"
import random

HAPPY_EMOJI_FACE: str = "\U0001f600"
SAD_EMOJI_FACE: str = "\U00002639"
EXCITED_EMOJI_FACE: str = "\U0000F929"
points: int
player: str


def main() -> None:
    """Main function will run all the designated functions!"""
    global points
    global player
    points = 0
    greet()
    choice: str = input("What option would you like to choose? 1: Play UNC Trivia! 2: Rules 3: Quit ")
    if choice == "1":
        i: int = 0
        while i < 5:
            if i == 0:
                question1()
            elif i == 1:
                points = question2(points)
            elif i == 2:
                points = question3(points)
            elif i == 3:
                points = question4(points)
            elif i == 4:
                points = question5(points)
            
            i += 1
            print(f"Your total adventure points = {points}")
        points = bonus_points(points)
        print(f"Your total adventure points = {points}")

    if choice == "2":
        rules()
  
    if choice == "3":
        print(f"Your total adventure points = {points}")
        quit()

 
def rules() -> None:
    """Rules of the quiz!"""
    input("Here are the rules! \n1. There are 5 questions.\n2. Each question is worth 10 points.\n3. If you get a question right, you earn 10 points.\n4.If you get a question wrong, you can try again but you get a 10 point penalty.\n5. Have fun!")


def greet() -> None:
    """Greeting the player and asking for the name!"""
    player = input("Welcome to UNC Trivia! A fun quiz game that will test your knowledge about UNC! What is your name?")
    print(f"Ok {player} let's begin!")
  

def question1() -> None:
    """Question 1 of the UNC Trivia Quiz."""
    global points
    answer: str = input("1. In what year was UNC found? A) 1789 B) 1834 C) 1993 D) 2001 ")

    if answer == "A" or answer == "a":
        points += 10
        print(f"That is correct!{HAPPY_EMOJI_FACE} UNC was found on December 11, 1789 ")
    else:
        points -= 10
        print(f"Incorrect! {SAD_EMOJI_FACE} The correct answer is A")


def question2(points: int) -> int:
    """Question 2" of the UNC Trivia Quiz."""
    points = points
    answer = input("2. What is the name of the UNC Mascot? A) Ramsey B) Ram C) Ramses D) Riverdale ")
    if answer == "C" or answer == "c":
        points += 10
        print(f"That is correct!{HAPPY_EMOJI_FACE} Ramses is the official name of the mascot for UNC! Go Tarheels!")
    else:
        points -= 10
        print(f"Incorrect! {SAD_EMOJI_FACE} The correct answer is C")
    return points


def question3(points: int) -> int:
    """Question 3 of the UNC Trivia Quiz."""
    points = points
    answer = input("3. If Chapel Hill wins a big game, which street do they celebrate at? A) Manning B) Franklin C) Andrews D) Angier ")
    if answer == "B" or answer == "b":
        points += 10
        print(f"That is correct! {HAPPY_EMOJI_FACE}On March 5, 2022, the UNC Tarheels defeated the Blue Devils 94-81 and celebrated the victory in Franklin Street at midnight!")
    else:
        points -= 10
        print(f"Incorrect! {SAD_EMOJI_FACE} The correct answer is B")
    return points


def question4(points: int) -> int:
    """Question 4 of the UNC Trivia Quiz."""
    points = points
    answer = input("4. What is the best course in UNC? (You better get this one right!) A) CHEM 101 B) COMP 110 C) MATH 233 D) IDST 101 ")
    if answer == "B" or answer == "b":
        points += 10
        print(f"That is correct! {HAPPY_EMOJI_FACE} COMP 110 is the best!")
    else:
        points -= 10
        print(f"Incorrect! {SAD_EMOJI_FACE} Really? Come on now... The correct answer is B")
    return points


def question5(points: int) -> int:
    """Question 5 of the UNC Trivia Quiz."""
    points = points
    answer = input("5. What is the name of the UNC newspaper? A) The Weekly Tar Heel B) The Yearly Tar Heel C) The Monthly Tarheel D) The Daily Tarheel ")
    if answer == "D" or answer == "d":
        points += 10
        print(f"That is correct! {HAPPY_EMOJI_FACE} Did you know that the Daily Tar Heel was originally called The Tar Heel?")
    else:
        points -= 10
        print(f"Incorrect! {SAD_EMOJI_FACE} The correct answer is D")
    return points


def bonus_points(points: int) -> int:
    """Bonus points added to the UNC Trivia quiz."""
    points = points
    print(f"Time for some bonus points! {EXCITED_EMOJI_FACE} Let's see how many bonus points you can get!")
    points += random.randint(0, 10)
    return points


if __name__ == "__main__":
    main()