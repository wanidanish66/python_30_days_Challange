class Employee:
    address = "kashmir"
    def add(self):
        print(f"the employee address is {self.address}")

    @property  # property turns the method into a read only attribute so instead of calling "e.name()" we call "e.name" makes the code cleaner
    def name(self):
        return f"{self.fname}, {self.lname}"  #This returns the full name using two attributes: fname lname
    
    @name.setter  # setter allows to assign value to name
    def name(self,value): # values recieve whaterver you assign
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()

e.name = "micro prob"  #python automatically calls the setter.
print(e.fname,e.lname)
