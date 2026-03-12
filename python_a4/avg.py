"""
Write a function to take a list of numbers and get the average. Use reduce function.
"""
from functools import reduce
nums=[23, 45, 66, 33, 20, 10]

total=reduce(lambda x,y : x+y , nums)
avg=total/len(nums)

print(avg)
