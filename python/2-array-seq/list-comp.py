"""
Built-In Sequences

* Container sequences (hold different data type)
- list
- tuple
- collections.deque

* Flat sequences (hold items of one simple type)
- str
- bytes
- array.array

Grouping in mutability:

* Mutable sequences
- list
- bytearray
- array.array
- collections.deque

* Immutable sequences
- tuple
- str
- bytes 
"""

# List comprehension
x = "ABC"
codes = [ord(c) for c in x]
codes = [last := ord(c) for c in x]  # Using :=, last can be have a local scope.
# c = exists only inside the listcomp
# last = exists outside the listcomp

# Generator Expressions (yield item using iterator protocol -> save memory than list comp)
genexp = tuple(ord(c) for c in x)
for o in genexp:
    print(o)

# Tuple as not just immutable list but records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32_450, 0.66, 8014)
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]
for passport in sorted(traveler_ids):
    print("%s/%s" % passport)  # % unpack tuple passport

# Tuple as immutable list
"""
An object is only hashable if its value cannot ever change

hash((10,[1,2])) # TypeError
hash((10, (1,2))) # True

Tuple support all list special methods except involving adding or removing or __reversed__
* This includes __add__, __getitem__, __iter__, __len__ etc... 
"""
a = (10, "alpha", [1, 2])  # mutable list inside immutable tuple
b = (10, "alpha", [1, 2])
b[-1][
    0
] = 1  # it will change value of contents of tuple b -> Tuple not always immutable!


# Unpacking sequences and iterables
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # unpacking iterable

t = (20, 8)
divmod(*t)  # Use * to unpack into function args

a, b, *rest = range(5)  # Use * to unpack excess items


def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


func(*[1, 2], 3, 4, *range(4, 7))  # Use * multiple time in function calls

list1 = [*range(4), 4]  # Use * to define list
tuple1 = (*range(40), 4)  # Use * to define tuple
set1 = {*range(4), 4, *(5, 6, 7)}  # Use * to define set
