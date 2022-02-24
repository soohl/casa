# Set theory

# Removing duplicates
l = ['a','a','b']
list(set(l))

# Set comprehension
from unicodedata import name
{chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}

# Return value of dict view can be used as a set 
d1 = dict(a=1,b=2,c=3,d=4)
d2 = dict(b=20,d=40,e=50)
d1.keys() & d2.keys() # {'b','d'}