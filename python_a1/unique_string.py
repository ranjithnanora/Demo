"""
7. Define a list of strings. Print out list of unique strings in the list.
• Test out using several lists of strings
"""

def unique_string(string_list):
    unique_list = list(set(string_list))
    print(unique_list)

unique_string(["apple", "banana", "apple", "cherry", "banana"])