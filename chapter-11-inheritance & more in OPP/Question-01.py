# this is a simple programm of multiple inheritance

class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"the value of x is {self.x} and the value of y is {self.y}")

class Vector3d(Vector2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def showZ(self):
        print(f"the value of x is {self.x} the value of y is {self.y} and  z is {self.z}")

a = Vector2d(3,5)
a.show()

b = Vector3d(2,4,5)
b.showZ()