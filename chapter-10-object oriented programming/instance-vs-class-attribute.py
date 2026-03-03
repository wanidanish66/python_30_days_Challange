class Employee:
    age = 22
    language = "python"

micro = Employee()
micro.language = "JavaScript"         # takes prefrence over class attribute during assignment and retrieval
print(micro.language,micro.age)       # here it prints language "JavaScript" instead of "python" because instance(object) attribute


# when looking up for micro.attribute it checks first if the attribute is present in the object and then checks 
# if the attribute is present in the class