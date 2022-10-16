"""EX 04: List Utility Functions: Practicing lists in functions.""" 


__author__ = "730546880" 


def all(list_of_integers: list[int], given_value: int) -> bool:
    """Locate if the given integer is in the list."""
    i: int = 0
    if len(list_of_integers) != 0:
        while i < len(list_of_integers):
            if list_of_integers[i] != given_value:
                return False

            i += 1
        return True
    else:
        return False

def max(given_list: list[int]) -> int:
    """Figure the maximum value in the given list."""
    if len(given_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maximum_value: int = given_list[i]
    while i < (len(given_list) - 1):
        if maximum_value < given_list[i+1]:
            maximum_value = given_list[i + 1]
        else:
            i += 1

    return maximum_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Compares two lists and see if they are similar values in their matching indexes."""
    if len(list_1) == len(list_2):
        i: int = 0
        while i < len(list_1 and list_2):
            if list_1[i] != list_2[i]:
                return False
            else:
                i += 1
        return True
    else:
        return False