"""EX05: List Utility Function: Practicing importing functions."""

__author__ = """730546680"""


def only_evens(given_list: list[int]) -> list[int]:
    """Return the integer in the given list, that is an even number."""
    i: int = 0
    even_list: list[int] = []
    while i < len(given_list):
        if given_list[i] % 2 == 0:
            even_list.append(given_list[i])
        i += 1
        
    return even_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns one list concantenating all the elements of the first list and all the elements in the second list."""
    concat_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        concat_list.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        concat_list.append(list_2[i])
        i += 1

    return concat_list


def sub(given_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns the substring list of the given list from the starting and ending indexes."""
    if len(given_list) == 0 or start_index > len(given_list) or end_index <= 0:
        return []
    
    sub_list: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(given_list):
        end_index = len(given_list)
    while start_index < end_index:
        sub_list.append(given_list[start_index])
        start_index += 1

    return sub_list