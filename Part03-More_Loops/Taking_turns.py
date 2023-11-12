""" Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

Sample output
Please type in a number: 5
1
5
2
4
3

Sample output
Please type in a number: 6
1
6
2
5
3
4 """

# Write your solution here

number = int(input("Please type in a number: "))

for i in range(1, number // 2 + 1):  # Loop only up to half of the number
    print(i)
    print(number + 1 - i)

if number % 2 == 1:  # If number is odd, print the middle number
    print(number // 2 + 1)


""" Solution for part03-27_taking_turns
src/taking_turns.py
number = int(input("Please type in a number: "))
 
left = 1
right = number
 
while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1
 
if left == right:
    print(left) """