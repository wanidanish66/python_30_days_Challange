class Employee:                           # it is highly recomended to name a class in pascal case
    age = 32
    salary = 2344323
    language = 'py'

micro = Employee                          # object 
micro.name = "micro wan"                  # here name is object attribute and language and age is class attribute as they directly belong to the class
print(micro.name,micro.age,micro.language)

adil = Employee
print(adil.language,adil.age)