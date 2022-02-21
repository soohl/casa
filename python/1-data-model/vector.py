# Special method when we want our object to support and interact with fundamental language constructs:

# For example, collections[key] is actually collections.__getitem__(key)

# Collection Abstraction Base Class defines three implementation:
# * Iterable to support loop and unpacking
# * Sized to support len
# * Container to support in

# Collection are:
# * Sequence (list, str)
# * Mapping (dict, collections.defaultdict)
# * Set (set and frozenset)

# These __XX__() functions are often called special method or magic method

# len() is not a special method since len() on built-in type is implemented directly
# by C backend for efficient operation. We can still implment __len__() to make len
# work on custom objects.

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
        x, y = self.x + other.x, self.y + other.y
        return Vector(x, y)

    def __mult__(self, scalar):
        """Does not modify self or other"""
        return Vector(x * scalar.y * scalar)
