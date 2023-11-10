""" Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test """


# Write your solution here

word = input("Please type in a string: ")
for i in range(len(word)):
    print(word[-i-1:])


""" Solution for part03-18_substrings_part_2
src/substrings_part_2.py
string = input("Please type in a string: ")
 
start = len(string) - 1
while start >= 0:
    print(string[start:])
    start -= 1 """