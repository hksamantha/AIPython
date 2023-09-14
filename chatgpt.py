def factorial(n):
    """
    Calculate the factorial of a non-negative integer 'n'.

    Args:
        n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial value of 'n'.

    Raises:
        ValueError: If 'n' is a negative integer.

    Example:
        factorial(5) returns 120
        factorial(0) returns 1
    """

    # Check if the input 'n' is a negative integer
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    # Initialize the result to 1
    result = 1

    # Multiply result by numbers from 1 to 'n'
    for i in range(1, n + 1):
        result *= i

    return result

# Example usage:
# Calculate the factorial of 5
result = factorial(5)
print(f"The factorial of 5 is {result}")






