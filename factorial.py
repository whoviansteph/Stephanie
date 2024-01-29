"""
Factorial Calculator Function

Objective:
Write a function named 'calculate_factorial' to compute the factorial of a number using a for loop.

Function Parameter:
1. number (integer): A non-negative integer for which the factorial is to be calculated.

Instructions:
- Use a for loop to calculate the factorial of 'number'.
- Return the factorial result.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. calculate_factorial(5) should return the factorial of 5.
2. calculate_factorial(0) should return 1.
3. calculate_factorial(3) should return the factorial of 3.
4. calculate_factorial(-1) should handle negative input.
"""


def calculate_factorial(number):
    # Handle edge cases for 0 and negative inputs
    if number < 0:
        return "Factorial is not defined for negative numbers."
    
    # Initialize the factorial result to 1
    factorial_result = 1

    # Calculate the factorial using a for loop
    for i in range(1, number + 1):
        factorial_result *= i

    return factorial_result

# Test cases
result1 = calculate_factorial(5)
print(f"Factorial of 5: {result1}")  # Expected output: 120

result2 = calculate_factorial(0)
print(f"Factorial of 0: {result2}")  # Expected output: 1

result3 = calculate_factorial(3)
print(f"Factorial of 3: {result3}")  # Expected output: 6

result4 = calculate_factorial(-1)
print(result4)  # Expected output: Factorial is not defined for negative numbers.
