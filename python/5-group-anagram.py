# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

from typing import DefaultDict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

dic = DefaultDict(list)

for s in strs:
    dic["".join(sorted(s))].append(s)

print([i for i in dic.values()])
