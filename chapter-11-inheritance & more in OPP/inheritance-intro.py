class Employee:
    company = "Rupa"
    salary = "300k"                # class attribute
    def show(self):
        self.salary = "400k"       # object attribute gets printed
        print(f"the name of the company is {self.company} and my salary is {self.salary}")

# class Programmer:
#     company = "Rupa corporation"
#     def show(self):
#         print(f"the name of the company is {self.company} and my salary is {self.salary}")
#     def showLanguage(self):
#         print(f"the name of the programmer is {self.name} and he is good with the language {self.language}")

# instead we can write like this
class Programmer(Employee):
    company = "Rupa corporation"
    def showLanguage(self,name,language):
        self.name = name
        self.language = language
        print(f"the name of the programmer is {self.name} and he is good with the language {self.language}")


a = Employee()
b = Programmer()

print(b.company)
b.show()
b.showLanguage("micro","python")