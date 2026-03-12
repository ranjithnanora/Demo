"""
Write a function with several string inputs. Function should return a string
with comma in between each string
"""

def combine_string(*words):
    result="\""
    for word in words:
        result+=word+","
    return result[:-1]+"\""

print(combine_string("first","second","third"))
print(combine_string("1","2","3","4","5"))