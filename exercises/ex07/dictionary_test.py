"""EX07: Dictionary Functions: Testing functions for dictionaries."""

__author__ = "730546880"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert() -> None:
    """Testing the function with a given dictionary and outputting a dictionary with inverted keys and values."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}
    xy: dict[str, str] = {'a': 'z', 'b': 'z', 'c': 'x'}
    assert(xy) == KeyError


def test_favorite_color() -> None:
    """Testing the function with a given dictionary and outputting the color is the common in the dictionary."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"
     

def test_count() -> None:
    """Testing the function with a given dictionary and outputting how many items are in each list."""
    xs: list[str] = ["red", "green", "blue", "green"]
    assert count(xs) == {"blue": 1, "green": 2, "red": 1}