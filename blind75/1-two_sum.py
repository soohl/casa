from pprint import pprint
from typing import List, DefaultDict
from collections import Counter
import re

nums: List[int] = [2, 7, 11, 15]
target: int = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: dict[int, int] = {}
        for i, num in enumerate(nums):
            if (target - num) in d:
                return [i, d.get(target - num)]
            else:
                d[num] = i


pprint(Solution().twoSum(nums, target))
