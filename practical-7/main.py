# Creating a dictionary
dict1 = {'name': 'John', 'age': 25, 'job': 'Engineer'}

# Printing the dictionary
print("Original Dictionary: ", dict1)

# Adding a new key-value pair
dict1['location'] = 'New York'
print("After adding a new key-value pair: ", dict1)

# Updating an existing key-value pair
dict1['age'] = 26
print("After updating an existing key-value pair: ", dict1)

# Removing a key-value pair
del dict1['job']
print("After removing a key-value pair: ", dict1)

# Checking if a key exists
if 'name' in dict1:
    print("'name' is a key in the dictionary")
else:
    print("'name' is not a key in the dictionary")

# Getting the value of a key
print("The value of 'name' is: ", dict1.get('name'))

# Getting the keys and values of the dictionary
print("Keys in the dictionary: ", dict1.keys())
print("Values in the dictionary: ", dict1.values())
