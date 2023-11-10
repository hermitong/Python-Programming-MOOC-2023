""" Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test """


# Write your solution here

word = input("Please type in a string: ")
for i in range(len(word)):
    print(word[:i+1])


""" Solution for part03-17_substrings_part_1
src/substrings_part_1.py
string = input("Please type in a string: ")
 
length = 1
while length <= len(string):
    print(string[0:length])
    length += 1 """