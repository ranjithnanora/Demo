"""
Do the same as question 4 with list comprehension
"""

models =[ "Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion"
         , "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

result= [model.split()[1] for model in models]
print(result)