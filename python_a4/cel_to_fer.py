"""
Write a function to convert a list of temperatures given in degree Celsius to Fahrenheit. 
Use list comprehension and lambda function.
"""

temp=[23,32,20,30]

fer=list(map(lambda x: (9/5)*x+32,temp))
print(fer)