"""EX05: List Utility Function: Practicing importing functions."""

__author__ = """730546680"""

from utils import only_evens
from utils import concat
from utils import sub


def test_even_numbers() -> None:
    """Testing the function with a given list and asserting even values."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_combined_list() -> None:
    """Testing the function with two given list and asserting the concatenation of the two lists."""
    xs: list[int] = [2, 3, 4, 5]
    xy: list[int] = [9, 4, 3, 2]
    assert concat(xs, xy) == [2, 3, 4, 5, 9, 4, 3, 2]


def test_substring_list() -> None:
    """Testing the function with a given list and returning a substring list."""
    xs: list[int] = [2, 4, 5, 9]
    assert sub(xs, 0, 3) == [2, 4, 5]
    
    