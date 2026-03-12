"""
Write a function to take a string and produce a list of ASCII codes 
for each character of the string.
"""

string="/hello world* abcd"

result=list(map(lambda x: ord(x),string))
print(result)