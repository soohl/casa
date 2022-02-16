from math import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x, self.y)

    def __repr__(self):
        """python will call __repr__ to print Vector if __str__ is not implmented"""
        return f"Vector({self.x},{self.y})"
    
    def __bool__(self):
        """Return True if absolute value is non-zero"""
        return bool(abs(self))

    def __add__(self, other):
        """Does not modify self or other"""
        x, y = self.x+other.x, self.y+other.y
        return Vector(x,y)

    def __mult__(self, scalar):
        """Does not modify self or other"""
        return Vector(x * scalar. y * scalar)