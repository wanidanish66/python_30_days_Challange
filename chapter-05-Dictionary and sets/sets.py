s = set() # Create an empty set
s.add(1) # Add an element to the set
s.add(2) # Add another element to the set
print(s) # Output: {1, 2}

# we can also create a set with initial values
s2 = {1, 2, 3, 4, 5}
print(s2) # Output: {1, 2, 3, 4, 5}

# sets do not allow duplicate values
s2.add(3) # This will not add 3 again to the set

# sets are unordered, so we cannot access elements by index
# but we can check if an element is in the set
print(1 in s2) # Output: True
print(6 in s2) # Output: False

# we can write string values in sets as well
s3 = {"apple", "banana", "cherry"}
print(s3) # Output: {'apple', 'banana', 'cherry'}