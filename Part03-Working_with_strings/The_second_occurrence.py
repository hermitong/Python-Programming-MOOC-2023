""" Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string. """


# Write your solution here
word = input("Please type in a string:")
sub = input("Please type in a substring:")

first_occ= word.find(sub)

if  first_occ != -1:
    second_occ = word.find(sub, first_occ + len(sub))
    if second_occ != -1:
        print(f"The second occurrence of the substring is at index {second_occ}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")


""" Solution for part03-22_second_occurrence
src/second_occurrence.py
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
 
index1 = string.find(substring)
index2 = -1
if index1 != -1:
    string = string[index1+len(substring):]
    index2 = string.find(substring)
 
if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".") """