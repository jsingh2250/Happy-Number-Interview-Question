# Read in positive integer.
# Sum up the squares of the digits. 
# Keep doing this until the number reaches 1 or starts repeating itself.
# If the number reaches 1, output 1. If the sequence repeats, output 0.

import sys

for line in sys.stdin:

    # Dictionary that stores numbers in the sequence.
    numbersInSequence = {}

    # Converts positive integer from string to integer.
    number = int(line)

    # Loops through Happy Number process until break condition is met.
    while True:

        # If the number reaches 1 in the Happy Number sequence, 
        # the input number is a happy number. Break the loop.
        if number == 1:
            isHappyNumber = 1
            break

        # Convert the number into a string of digits.
        digits = str(number)

        # Set the number to 0 before summing the squares of the digits.
        number = 0

        # Sum the square of the digits of the number.
        for digit in digits:
            number += int(digit) ** 2

        # If the number has appeared in the sequence previously,
        # the sequence has started repeating.
        # The number is not a happy number. Break the loop.
        if number in numbersInSequence.keys():
            isHappyNumber = 0
            break
        
        # Store the current number in the sequence as a key in the dictionary.
        numbersInSequence[number] = True

    # Print 1 if the input number was a happy number.
    # Print 0 if the input number was not a happy number.
    print(isHappyNumber)