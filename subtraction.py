"""
This module contains a function for subtracting two numbers.
"""

def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.

    Args:
        a (float): The number from which to subtract.
        b (float): The number to subtract.

    Returns:
        float: The result of a - b.
    """
    return a - b

if __name__ == "__main__":
    # Example usage
    NUM1 = 10.5  # Constant
    NUM2 = 4.5   # Constant
    print(f"The result of subtracting {NUM2} from {NUM1} is {subtract(NUM1, NUM2)}")
