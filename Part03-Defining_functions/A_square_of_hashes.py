""" Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.

hash_square(3)
print()
hash_square(5)
Sample output
###
###
###

#####
#####
#####
#####
##### """

# Write your solution here
def hash_square(i):
    for m in range(0, i ):
        print(i * "#")
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)


""" Solution for part03-32_square_of_hashes
src/square_of_hashes.py
def hash_square(size):
    tows = size
    while tows > 0:
        print("#" * size)
        tows -= 1
 
if __name__ == "__main__":
    hash_square(5) """