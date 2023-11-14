""" Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

squared("ab", 3)
print()
squared("aybabtu", 5)
Sample output
aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba """

import math

def squared(inp: str, n: int):
    if len(inp) == 0:
        raise ValueError("Input string must have 1 or more characters")

    inp = inp * math.ceil(n / len(inp))
    for i in range(n):
        print(inp[:n])
        inp = inp[n:] + inp[:n]

""" Solution for part03-34_word_squared
src/word_squared.py
def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)
# Write your solution here """