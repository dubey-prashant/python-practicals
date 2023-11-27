# Creating a list
list1 = ['apple', 'banana', 'cherry']

# Printing the list
print("Original List: ", list1)

# Adding an element to the end of the list
list1.append('dragonfruit')
print("After adding an element: ", list1)

# Removing an element from the list
list1.remove('banana')
print("After removing an element: ", list1)

# Inserting an element at a specific position
list1.insert(1, 'blueberry')
print("After inserting an element: ", list1)

# Sorting the list
list1.sort()
print("After sorting the list: ", list1)

# Reversing the list
list1.reverse()
print("After reversing the list: ", list1)

# Counting the number of occurrences of an element
count = list1.count('apple')
print("Count of 'apple': ", count)

# Finding the index of an element
index = list1.index('cherry')
print("Index of 'cherry': ", index)
