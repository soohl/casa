# Converting Int List to Int

import functools

l = [1, 2, 3, 4]

# #1 way
result = "".join(str(e) for e in l)
print(int(result))

# #2 way
result = "".join(map(str, l))
print(int(result))

# #3 way
result = functools.reduce(lambda x, y: 10 * x + y, l, 0)
print(result)
