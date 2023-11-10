""" Please write a program which asks the user for a string and an amount. The program then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added.

An example of expected behaviour:

Sample output
Please type in a string: hiya
Please type in an amount: 4
hiyahiyahiyahiya """

# Write your solution here

string = input("Please type in a string:")
number = int(input("Please type in an amount:"))

print(string * number)
#return string * number

""" Solution for part03-08_string_multiplied
src/string_multiplied.py
input_string = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
print (input_string * amount) """