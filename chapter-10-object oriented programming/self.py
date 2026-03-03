class Employee:
    age = 22
    language = "python"
    def getInfo(self):          # while creating a method inside the class we have to to use self parameter
        print(f"my language is {self.language} and my age is {self.age}")

micro = Employee()
print(micro.language,micro.age)       
micro.language = "JavaScript"  

micro.getInfo()                 # self parameter is automatically passed during the function call