"""
Use the models list and make a comma separated string of car model names without make. 
“Civic,Accord,Corolla,Camry, Fusion,Escape,Sentra,Elantra”. Use reduce function.
"""
from functools import reduce
models =[ "Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion"
         , "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

result=reduce(lambda x,y: x+","+y.split()[1], models, "")[1:]
print(result)