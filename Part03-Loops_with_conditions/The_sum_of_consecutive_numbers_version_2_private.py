""" Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Sample output
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

You may assume the number typed in by the user is always equal to 2 or higher. """

# Write your solution here

# Ask the user for a limit
limit = int(input("Limit: "))

# Initialize the sum and the current number
sum_numbers = 0
current_number = 0

number = []

while sum_numbers < limit:
    current_number += 1
    sum_numbers += current_number
    number.append(str(current_number))

# Print the sum
print("The consecutive sum: " + " + ".join(number)+f" = {sum_numbers}")