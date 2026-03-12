"""
Write a function to make a dictionary that has key as the make and value as the model. 
Use zip, dictionary comprehension.
"""

makes = ["Honda", "Toyota", "Ford", "Nissan", "Hyundai"]
models =[ "Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion"
         , "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

def gen_dict(makes: list, models: list):
    return {
        make : [model for model in models if model.startswith(make)] for make in makes
    }

print(gen_dict(makes,models))