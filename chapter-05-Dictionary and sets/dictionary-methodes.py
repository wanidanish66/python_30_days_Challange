# methods in dictionary

a = {
    "name": "micro",
    "age": 25,
    "city": "kashmir",
    "marks" : [90, 80, 85, 95, 88]
}

print(a) #this prints the whole dictionary
print(a.items()) #this prints all the key-value pairs in the dictionary as a list of tuples
print(a.keys()) #this prints all the keys in the dictionary
print(a.values()) #this prints all the values in the dictionary

print(a["name"]) #this prints the value of the key "name"
print(a.get("age")) #this also prints the value of the key "age"

print(a.update({"age": 26})) #this updates the value of age to 26
print(a) #this prints the updated dictionary