"""
Write a function to convert a string to an array of ASCII codes
"""

def String_ASCII(word: str)->list:
    ASCII_arr=[]
    for letter in word:
        ASCII_arr.append(ord(letter))
    return ASCII_arr

words=["Hello", "World", "Name", "ABCDabcd"]
for word in words:
    print(String_ASCII(word))