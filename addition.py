"""
This module contains a function for adding two numbers.
"""

def add(a: float, b: float) -> float:
    """
    Adds two numbers together.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    # Example usage
    NUM1 = 10.5  # Constant
    NUM2 = 4.5   # Constant
    print(f"The sum of {NUM1} and {NUM2} is {add(NUM1, NUM2)}")
