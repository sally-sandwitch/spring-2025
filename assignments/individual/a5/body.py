"""Two-dimensional simulation of gravitational forces acting on a particular
body."""

import math
from vector import Vector 

# Gravitational constant
G = 6.6743e-11  # N⋅m^2/kg^2

class Body:
    def __init__(self, mass : float, p0 : Vector, v0 : Vector):
        """Create a new body of given mass in kg, given position in (m, m),
        and given velocity in (m/s, m/s)."""
        self.mass = mass
        self.p = p0
        self.v = v0

    def force_with(self, other):
        """Return the force in (N, N) exerted by the other body on this body."""
        dis=self.p.distance_to(other.p)
        sub=self.p-other.p
        m1 = self.mass
        m2 = other.mass
        f = G*m1*m2/dis**2
        return sub.times(-f/dis)

    def force_with_all(self, other):
        """Return the force in (N, N) exerted by all the other bodies on this
        body."""
        f = Vector(0.0, 0.0)
        for b in other:
            f+=self.force_with(b)
        return f

    def update_position(self, f : Vector, dt : float):
        """Update the position of this body based on the total force (fx, fy)
        imparted on it and assuming `dt` seconds have elpased."""
        a=f.times(1/self.mass) 
        dv= a.times(dt)
        self.v += dv
        dx= self.v.times(dt)
        self.p += dx

    def pos(self):
        """Return the position in (m, m) of this body."""
        return self.p

    def __str__(self):
        """Return a string describing this body."""
        s = str(self.mass) + ' at '
        s += str(self.p) + ' velocity '
        s += str(self.v) 
        return s

def new_position(bodies : list[Body], dt : float):
    """Compute the new position of all bodies in our system."""
    forces = []
    for i in range(len(bodies)):
        others = bodies[:]
        others.pop(i)
        forces.append(bodies[i].force_with_all(others))
    for i in range(len(bodies)):
        bodies[i].update_position(forces[i], dt)

def main():
    # A simple test case based on information found below.
    # https://qsstudy.com/gravitational-force-sun-earth/
    # https://en.wikipedia.org/wiki/Orbital_speed
    sun = Body(1.99e30, Vector (0.0, 0.0), Vector (0.0, 0.0))
    earth = Body(5.96e24, Vector (1.497e11, 0.0), Vector (0.0, 29800.0))
    print(earth)
    print(earth.force_with(sun))

if __name__ == '__main__':
    main()
