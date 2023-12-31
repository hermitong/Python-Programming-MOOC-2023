""" Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:

Sample output
Limit: 2
3

Sample output
Limit: 10
10

Sample output
Limit: 18
21

If you have trouble understanding how the desired output is calculated, the sample outputs in the next exercise may help. You may assume the number typed in by the user is always equal to 2 or higher. """

# Ask the user for a limit
limit = int(input("Limit: "))

# Initialize the sum and the current number
sum_numbers = 0
current_number = 0

# Loop until the sum is at least equal to the limit
while sum_numbers < limit:
    current_number += 1
    sum_numbers += current_number

# Print the sum
print(sum_numbers)