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
    num1 = 10.5
    num2 = 4.5
    print(f"The result of subtracting {num2} from {num1} is {subtract(num1, num2)}")
