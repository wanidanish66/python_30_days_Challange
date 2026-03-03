class Employee:
    age = 22
    language = 'python'
    @staticmethod      #sometime we need a function that doesnot use self parameter . we can define static mode like this
    def info():
        print(f"my age is {Employee.age}")

print(Employee.age,Employee.language)
Employee.info()