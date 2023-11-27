# Creating a tuple
tuple1 = ('apple', 'banana', 'cherry')

# Printing the tuple
print("Original Tuple: ", tuple1)

# Accessing an element of the tuple
print("Element at index 1: ", tuple1[1])

# Counting the number of occurrences of an element
count = tuple1.count('apple')
print("Count of 'apple': ", count)

# Finding the index of an element
index = tuple1.index('cherry')
print("Index of 'cherry': ", index)

# Note: Tuples are immutable, which means you can't add, remove, or change elements after the tuple is defined.
