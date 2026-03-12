"""
Write a function that takes variable number of strings and one string
separator. Function should return a string with the separator string inserted
between each string input.
"""

def combine_string( seprator, *words,):
    result="\""
    print("\"",*words, "\"", sep=seprator)
    # for word in words:
    #     result+=word+seprator
    # return result[:-1]+"\""
    return None

print(combine_string("|","first","second","third"))
print(combine_string("*","1","2","3","4","5"))