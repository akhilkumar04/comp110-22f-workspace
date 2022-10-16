"""EX07: Dictionary Functions: Testing functions for dictionaries."""
__author__ = "730546880"


def invert(given_dictionary: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary that inverts the keys and values."""
    inverted_dict: dict[str, str] = {}
    for key in given_dictionary: 
        if key in inverted_dict:
            raise KeyError("Key Error!")
        
        inverted_dict[given_dictionary[key]] = key

    return inverted_dict


def favorite_color(given_dictionary: dict[str, str]) -> str:
    """Returns the most frequent color in a dictionary."""
    frequency_dictionary: dict[str, str] = {}
    for name in given_dictionary:
        if given_dictionary[name] in frequency_dictionary:
            frequency_dictionary[given_dictionary[name]] += 1
        else:
            frequency_dictionary[given_dictionary[name]] = 1
    
    color: str = ""
    frequency: int = 0
    for name in frequency_dictionary:
        if frequency_dictionary[name] > frequency:
            frequency = frequency_dictionary[name] 
            color = name
    return color
            

def count(given_list: list[str]) -> dict[str, int]:
    """Returns the number of times each value appears on the list."""
    values: dict[str, int] = {}
    for item in given_list:
        if item in values:
            values[item] += 1
        else:
            values[item] = 1
    return values