#Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

#The beginning of your output should look like this:

#Sample output

#2
#4
#6
#8
#etc...

# Write your solution here

for number in range(2, 31):# The even numbers start from 2 to 30, thus 30 is include in the range
    if number % 2 == 0:    # to test whether an even number 
        print(number)
    number += 1            # repeat print?