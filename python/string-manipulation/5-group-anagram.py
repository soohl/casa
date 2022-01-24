"""
Group by anagrams 
Time Complexity: O(n)

Notes:
"""

from typing import DefaultDict

# Input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


################################################
dic = DefaultDict(list)

for s in strs:
    dic["".join(sorted(s))].append(s)

print(list(dic.values()))
################################################
