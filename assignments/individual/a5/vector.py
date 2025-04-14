import math

"""authors == Adriana"""

class Vector:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'<{self.x}, {self.y}>'

    def __str__(self):
        return self.__repr__()
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y 
    
    def set_x(self,new_x):
        self.x=new_x

    def set_y(self,new_y):
        self.y=new_y
    
    def __eq__(self,other):
        if (self.x==other.x and self.y==other.y):
            return self.__repr__() == other.__repr__()
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) 
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y) 

    def times(self, time):
       return Vector(self.x * time, self.y * time) 
    
    def distance_to(self,other):
        return math.sqrt(((other.x - self.x)**2) + ((other.y - self.y)**2))
