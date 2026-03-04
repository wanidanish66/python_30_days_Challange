# this is multiLevel inheritance

class Employee:       # this is a parent class
    company = "Rupa"
    salary = "300k"                # class attribute
    def show(self):
        self.salary = "400k"       # object attribute gets printed
        print(f"the name of the company is {self.company} and my salary is {self.salary}")

class Address(Employee):       # this is a child class and also a parent class
    address = "kashmir"
    def add(self):
        print(f"the employee address is {self.address}")

class Programmer(Address):        # this is a child class 
    company = "Rupa corporation"
    def showLanguage(self,name,language):
        self.name = name
        self.language = language
        print(f"the name of the programmer is {self.name} and he is good with the language {self.language}")


a = Employee()
b = Programmer()
c = Address() 

print(b.company)
b.show()
c.show()
b.add()
b.showLanguage("micro","python")