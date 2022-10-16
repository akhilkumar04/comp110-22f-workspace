"""An example of a list utility program."""

# Name: contains
# Function with two parameters:
# needle - what we're searching for 
# hay stack - what we're searching through
# Return Type: bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Start fron first index
    i: int = 0
# Loop thorugh each index of teh list
    while i < len(haystack):
        # Test if equal to needle
        if haystack[i] == needle:
        # Yes! Return True
            return True
    # Return False
    return False