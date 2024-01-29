"""
Compound Interest Calculator Function

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.
2. r (float): Annual interest rate in decimal.
3. n (integer): Number of times interest is compounded per year.
4. t (integer): Number of years for investment.

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""


import sys

def compound_interest_calculator(P, r, n, t):
    # Check for valid inputs
    if P <= 0 or r < 0 or n <= 0 or t <= 0:
        print("Invalid input. Please provide positive values for Principal, Annual interest rate, Number of times interest is compounded, and Number of years.")
        sys.exit()

    # Calculate compound interest using the formula
    A = P * (1 + r/n)**(n*t)
    
    return A

# Test cases
result1 = compound_interest_calculator(1000, 0.05, 12, 5)
print(f"Result 1: ${result1:.2f}")  # Expected output: Amount after 5 years

result2 = compound_interest_calculator(500, 0.07, 4, 10)
print(f"Result 2: ${result2:.2f}")  # Expected output: Amount after 10 years

result3 = compound_interest_calculator(1500, 0.03, 6, 7)
print(f"Result 3: ${result3:.2f}")  # Expected output: Amount after 7 years

