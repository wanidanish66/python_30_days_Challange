class Employee:
    age = 22      # this is class attribute
    language = 'python'
 
    def __init__(self, name, language, age):      # this is known as dunder method which runs automatically as soon as the object is created
        self.name = name
        self.language = language
        self.age = age
        print("i am creating an object")        

micro = Employee('micro','javaScript',33)

print(micro.name,micro.age,micro.language)