s = {1, 8, 2, 3, 4, 5}

print(len(s)) # Output: 6
s.add(6) # Add an element to the set
print(s) # Output: {1, 2, 3, 4, 5, 6}

s.remove(8) # Remove an element from the set
print(s) # Output: {1, 2, 3, 4, 5, 6}

s.pop() # Remove and return an arbitrary element from the set
print(s) # Output: {2, 3, 4, 5, 6}

s.clear() # Remove all elements from the set
print(s) # Output: set()