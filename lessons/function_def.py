"""An example function definition"""


def my_max(a: int, b: int) -> int:
    """Return the largest argument"""
    if a >= b:
        return a
    
    return b

print(my_max(10, 0))


