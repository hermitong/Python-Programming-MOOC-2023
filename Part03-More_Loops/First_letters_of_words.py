""" Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w """

# Write your solution here
sentence = input("Please type in a sentence: ")

word = ""
for char in sentence:
    if char != " ":
        word += char
    else:
        if word != "":
            print(word[0])
            word = ""

# Print the first letter of the last word
if word != "":
    print(word[0])

#sentence = input("Please type in a sentence: ")

#words = sentence.split()

#for word in words:
    #first_letter = word[0]
    #print(first_letter)

""" Solution for part03-24_first_letters_of_words
src/first_letters_of_words.py
sentence = input("Please type in a sentence: ")
 
# Add a space at the start, to make handling sentence easier
sentence = " " + sentence
 
# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1 """