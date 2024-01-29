"""
Leap Year Checker Function

Objective:
Write a function named 'is_leap_year' to determine whether a given year is a leap year.

Function Parameter:
year (integer): The year to be checked.

Instructions:
- The function should return 'True' if the 'year' is a leap year and 'False' otherwise.
- A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.
- Use conditional statements to implement the leap year check.

Example Test Cases:
1. is_leap_year(2020) should return 'True'.
2. is_leap_year(1900) should return 'False'.
3. is_leap_year(2000) should return 'True'.
4. is_leap_year(2019) should return 'False'.
"""


def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if it is a century year
        if year % 100 == 0:
            # Check if it is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test cases
result1 = is_leap_year(2020)
print(f"Is 2020 a leap year? {result1}")  # Expected output: True

result2 = is_leap_year(1900)
print(f"Is 1900 a leap year? {result2}")  # Expected output: False

result3 = is_leap_year(2000)
print(f"Is 2000 a leap year? {result3}")  # Expected output: True

result4 = is_leap_year(2019)
print(f"Is 2019 a leap year? {result4}")  # Expected output: False
