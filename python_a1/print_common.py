"""
6. Define two list of numbers. Print out the numbers common to both lists.
• Test out using several list examples
"""

def print_common(list1, list2):
    common = list(set(list1).intersection(list2))
    print(common)

print_common([1, 2, 3, 4, 5, 6], [4, 4, 5, 6, 7, 8])
print_common([10, 20, 30], [40, 50, 60])
print_common([1, 2, 2, 3], [2, 3, 3, 4])