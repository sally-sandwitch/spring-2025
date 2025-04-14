import math

class Shape:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return 'indefined'
    


class Circle(Shape):
    "radius = r"
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.radius=r

    def area(self):
        return math.pi* self.radius**2
    
c=Circle(0.,0.,1.0)
print(c.area())
