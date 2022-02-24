dial_codes = [
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United States"),
]

country_dial = {country: code for code, country in dial_codes}
sorted_country_dial = {code:country.upper() in sorted(country_dial.items())}

def dump(**kwargs):
    return kwargs

print(dump(**{'x':1}, y=2, **{'z':3}))# == dump(x=1, y=2, z=3)
print({'a': 0, **{'x':1}, 'y':2, **{'z':3, 'x':4}}) # {'a':0, 'x':4, 'z':3}

# Merging dict 
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 | d2 # {'a': 2, 'b': 4, 'c': 6}
d1 |= d2 # Merge in-plce d1 


# Pattern matching with dict
def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

# Pattern matching and return dict
food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')

# Hashable
tt = (1,2,(30,40)) # hashable because all items are immutable
t1 = (1,2,[30,40]) # not hashable because list is mutable
t2 = (1,2, frozenset([30,40])) # hashable because frozenset is hashable

# dict.setdefault; if item not found, return []
index = {}
key = [1,2,3]
index.setdefault(key, []).append((1,2))
"""
if key not in index:
    index[key] = []
index[key].append((1,2))
"""

# collections.defaultdict; alternative to setdefault
from collections import defaultdict
index = defaultdict(list)
index[key].apend((1,2))

# collections.ChainMap; holds a list of mapping that can be searched as one; 
from collections import ChainMap
d1 = dict(a=1,b=3)
d2 = dict(a=2,b=4,c=6)
chain = ChainMap(d1,d2)
chain['a'] # 1
chain['c'] # 6

# collections.Counter; holds an integer count for each key
from collections import Counter
ct = Counter('abracadabra')
ct.most_common(3) # [('a', 5), ('b', 2), ('r', 2)]

# Making immutable mappings
from types import MappingProxyType
d = {'a': 1}
d_proxy = MappingProxyType(d)
d_proxy['a'] = 2 # TypeError 

# Dictionary View; Allow high performance operations on dict without unnecessory copying of data
d = dict(a=10,b=20,c=30)
values = d.values() # return dict_values([10,20,30]) which is a dict view 