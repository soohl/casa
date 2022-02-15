# Swapping Variables

# 1 way
a = 0
b = 10
a, b = b, a
print(a, b)

# 2 way (only numbers)
x = 1
y = 5
x += y
y = x - y
x -= y
print(x, y)
