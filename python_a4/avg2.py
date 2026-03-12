"""
Write a function to take a list of numbers and get the average of all positive 
numbers in the list. Use reduce function.
"""

from functools import reduce
nums=[23, 45, -66, 33, 20, 10]

total, count= reduce(lambda x,y: (x[0]+y, x[1]+1) if y>0 else x, nums, (0,0))
#print(total, count)
avg= total/count if count!=0 else 0
print(avg)

nums=[1,1,2,3,4,4,5,6,7,7]
map={}
map=reduce(lambda map,x: {**map, x:map.get(x,0)+1}, nums, {})
print(map)