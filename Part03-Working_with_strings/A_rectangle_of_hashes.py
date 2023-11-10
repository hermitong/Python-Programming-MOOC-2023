""" Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
########## """


# Write your solution here

width = int(input("Width:"))
height = int(input("Height:"))
i = 0

while i < height:
    print("#" * width)
    i += 1


""" Solution for part03-13_rectangle_of_hashes
src/rectangle_of_hashes.py
width = int(input("Width: "))
height = int(input("Height: "))
 
n = 0
while n < height:
    print("#" * width)
    n += 1 """