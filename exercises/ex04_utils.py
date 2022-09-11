"""EX 04: List Utility Functions: Practicing lists in functions""" 


__author__ = "730546880" 

from random import randint


def all(list_of_integers: list[int], given_value: int) -> bool:
    """Locate if the given integer is in the list."""
    i: int = 0
    while i < len(list_of_integers):
        if list_of_integers[i] == given_value:
            return True
        else:
             i += 1
    return False

def max(given_list: list[int]) -> int:
    """Figure the maximum value in the given list."""
    if len(given_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maximum_value: int = given_list[i]
    while i < len(given_list):
        if maximum_value < given_list[i+1]:
            maximum_value = given_list[i+1]
            return maximum_value
        else:
            i += 1
    
def is_equal(list_1: list[int], list_2: list[int]):
    """Compares two lists and see if they are similar values in their matching indexes."""
    i: int = 0
    while i < len(list_1 and list_2):
        if list_1[i] == list_2[i]:
            return True
        else:
            return False


