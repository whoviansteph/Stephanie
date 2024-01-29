"""
Speeding Ticket Function

Objective:
Write a function named 'speeding_ticket' that evaluates whether a driver should receive a speeding ticket based on their driving speed and a special condition (their birthday).

Function Parameters:
1. speed (integer): The driver's speed in mph (miles per hour).
2. is_birthday (boolean): A flag indicating whether the driver is driving on their birthday.

Instructions:
- The function should return one of three strings based on the driver's speed: "No Ticket", "Small Ticket", or "Big Ticket".
- If the driver's speed is 60 mph or less, they should receive "No Ticket".
- If the driver's speed is between 61 and 80 mph inclusive, they should receive a "Small Ticket".
- If the driver's speed is 81 mph or more, they should receive a "Big Ticket".
- On the driver's birthday, the speed limits for each ticket category are increased by 5 mph. For example, they can go up to 65 mph and still receive "No Ticket" if is_birthday is True.

Example Test Cases:
1. speeding_ticket(60, False) should return "No Ticket".
2. speeding_ticket(75, False) should return "Small Ticket".
3. speeding_ticket(85, False) should return "Big Ticket".
4. speeding_ticket(65, True) should return "No Ticket".
5. speeding_ticket(85, True) should return "Small Ticket".
"""


def speeding_ticket(speed, is_birthday):
    # Adjust speed limits on the birthday
    if is_birthday:
        speed -= 5

    # Evaluate speeding ticket based on speed
    if speed <= 60:
        return "No Ticket"
    elif 61 <= speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Test cases
result1 = speeding_ticket(60, False)
print(result1)  # Expected output: "No Ticket"

result2 = speeding_ticket(75, False)
print(result2)  # Expected output: "Small Ticket"

result3 = speeding_ticket(85, False)
print(result3)  # Expected output: "Big Ticket"

result4 = speeding_ticket(65, True)
print(result4)  # Expected output: "No Ticket"

result5 = speeding_ticket(85, True)
print(result5)  # Expected output: "Small Ticket"
