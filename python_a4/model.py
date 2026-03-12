"""
Write a function to make a list of all models without the make name. Use map, lambda function 
to create the list
"""

models =[ "Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion"
         , "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

def extract_models(models: list)->list:
    return list(map(lambda x: x.split()[1], models))

print(extract_models(models))