"""
Fibonacci Sequence Calculator Function

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""


def fibonacci_sequence(max_value):
   def fibonacci_sequence(max_value):
    # Handle edge cases for 0 and negative inputs
    if max_value < 0:
        return "Invalid input. Please provide a non-negative value."

    # Initialize the Fibonacci sequence
    sequence = []

    # Initialize the first two Fibonacci numbers
    fib1, fib2 = 0, 1

    # Generate the Fibonacci sequence up to max_value using a while loop
    while fib1 <= max_value:
        sequence.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2

    return sequence

# Test cases
result1 = fibonacci_sequence(10)
print(f"Fibonacci sequence up to 10: {result1}")  # Expected output: [0, 1, 1, 2, 3, 5, 8]

result2 = fibonacci_sequence(1)
print(f"Fibonacci sequence up to 1: {result2}")  # Expected output: [0, 1, 1]

result3 = fibonacci_sequence(0)
print(f"Fibonacci sequence up to 0: {result3}")  # Expected output: [0]

result4 = fibonacci_sequence(-5)
print(result4)  # Expected output: Invalid input. Please provide a non-negative value.



# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
