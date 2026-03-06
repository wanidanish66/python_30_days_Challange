# this is a programme to use property decorators

class Employee:
    salary = "300k"

    @property
    def salaryAfterIncrement(self):
        return f"the salary after increament is {self.salary}"
    
    @salaryAfterIncrement.setter  
    def salaryAfterIncrement(self,value): 
        self.salary = value

s = Employee()
s.salaryAfterIncrement = "500k"

print(s.salary)
