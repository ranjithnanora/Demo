"""
Take a list of names in the format “firstname lastname”. Then make a dictionary with key as the
last name and value as the first name
"""

first_names = ["Ranjith", "Rhoit", "Priya", "Karthik", "Sneha"]
last_names = ["Kumar", "Sharma", "Reddy", "Iyer", "Patel"]

name_dict=dict(zip(last_names, first_names))
print(name_dict)