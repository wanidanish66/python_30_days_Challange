# new operator | and | = allow for merging and updating dictionaries:

dict1 = {"a": 4, "b": 3}
dict2 = {"b": 3, "c": 8} 

merge = dict1 | dict2
print(merge)

# output will be : {"a": 4, "b": 3, "c": 8}
