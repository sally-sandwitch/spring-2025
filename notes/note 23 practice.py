import math

#class Complex:
#    def __init__(self, real : float, imag : float=0.0):
#        self.real = real
#        self.imag = imag

#    def __repr__(self):
#        return '({:.3f}{:+.3f}i)'.format(self.real, self.imag)

#    def __str__(self):
#        return self.__repr__()
#
#    def __add__(self, other):
#        return Complex(self.real + other.real, self.imag + other.imag)
#
#    def conjugate(self):
#        return Complex(self.real, -self.imag)
    
#c1=Complex(1.3,-1.768)
#print(c1+c1)
#print(c1.__add__(c1))
#c2=Complex(2.3893)
#print(c2)



class Circle:
    def __init__(self,radius:float):
        self.radius=radius
    
    def get_radius(self):
        return self.radius
    def set_radius(self,new_radius):
        self.radius=new_radius

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2*math.pi * self.radius
        

c1=Circle(10.0)

print(type(c1))
print(c1.area())
print(c1.circumference())
c1.set_radius(2.0)
print(c1)