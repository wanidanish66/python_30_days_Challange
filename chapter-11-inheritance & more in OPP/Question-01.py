# this is a simple programm of multiple inheritance

class Vector2d:
    x = 4
    y = 5
    def show(self):
        print(f"the value of x is {self.x} and the value of y is {self.y}")

class Vector3d(Vector2d):
    def showZ(self,z):
        self.z = z
        print(f"the value of z = {self.z}")

a = Vector2d()
b = Vector3d()

print(b.x,b.y)
b.show()
b.showZ("6")