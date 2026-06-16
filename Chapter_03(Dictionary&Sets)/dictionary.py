my_dict = {"name": "Sifat", "age": 25, "city": "Dhaka"}
print(my_dict)
# Accessing values in a dictionary
print(my_dict["name"]) # Sifat 
print(my_dict.get("age")) # 25
# Adding a new key-value pair to the dictionary
my_dict["country"] = "Bangladesh"
print(my_dict)
# Updating a value in the dictionary
my_dict["age"] = 26     
print(my_dict)
# Removing a key-value pair from the dictionary
del my_dict["city"]
print(my_dict)
# Functions for dictionaries
print(my_dict.keys()) # dict_keys(['name', 'age', 'country'])
print(my_dict.values()) # dict_values(['Sifat', 26, 'Bangladesh'])
print(my_dict.items()) # dict_items([('name', 'Sifat'), ('age', 26), ('country', 'Bangladesh')])    
print(len(my_dict)) # 3
