#lists are containers to store a set of values of any data type.

list = ["apple", "Micro", "google", 8, 9.5, True]
print(list)

# lists are mutable, which means we can change the values in the list after it has been created.
list[0] = "banana"
print(list)

# list indexing is simar to string indexing, we can access the values in the list using their index.
print(list[0]) # prints the first element in the list
print(list[1]) # prints the second element in the list
print(list[2]) # prints the third element in the list
print(list[-1]) # prints the last element in the list
print(list[-2]) # prints the second last element in the list
print(list[-3]) # prints the third last element in the list
print(list[2:5]) # prints the elements from index 2 to index 4 (5 is not included)
print(list[:3]) # prints the first three elements in the list