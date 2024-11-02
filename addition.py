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
    num1 = 10.5
    num2 = 4.5
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
