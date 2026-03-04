# this is multiple inheritance

class Employee:
    company = "Rupa"
    salary = "300k"                # class attribute
    def show(self):
        self.salary = "400k"       # object attribute gets printed
        print(f"the name of the company is {self.company} and my salary is {self.salary}")

class Address:
    address = "kashmir"
    def add(self):
        print(f"the employee address is {self.address}")

class Programmer(Employee,Address):
    company = "Rupa corporation"
    def showLanguage(self,name,language):
        self.name = name
        self.language = language
        print(f"the name of the programmer is {self.name} and he is good with the language {self.language}")


a = Employee()
b = Programmer()

print(b.company)
b.show()
b.add()
b.showLanguage("micro","python")