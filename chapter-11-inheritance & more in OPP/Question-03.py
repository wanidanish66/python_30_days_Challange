# this is a programme to use property decorators

class Employee:
    salary = 30000
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter  
    def salaryAfterIncrement(self,salary): 
        self.increment = ((salary / self.salary) -1) *100

s = Employee()
print(s.salaryAfterIncrement)

s.salaryAfterIncrement = 306000
print(s.increment)
