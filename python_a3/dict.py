"""
A dictionary key and value are both strings. Write a function that takes
variable number of arguments. Each argument will be passed as named
arguments. Function must return true if all keys in the function input exists
and values match the value specified. It must return a false if either a key
does not exist or the value does not match.
"""

def key_value_exists(target_dict, **kwargs):
    if not kwargs:
        return True
        
    for key, value in kwargs.items():
        if key not in target_dict:
            return False
    
        if str(target_dict[key]) != str(value):
            return False
        
    return True

data = {"a": "1", "b": 2, "c": 3, "z": 26}

print(f"Test 1 (b='2'): {key_value_exists(data, b='2')}")      
print(f"Test 2 (a=1, z=26): {key_value_exists(data, a=1, z=26)}") 
print(f"Test 3 (a=2): {key_value_exists(data, a=2)}")          
print(f"Test 4 (a=1, d=4): {key_value_exists(data, a=1, d=4)}") 