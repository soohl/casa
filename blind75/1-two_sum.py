from pprint import pprint
from typing import List, DefaultDict
from collections import Counter
import re

"""
Time Complexity: O(n)
"""

# Input
nums = [2, 7, 11, 15]

# Output
target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if (target - num) in d:
                return [i, d.get(target - num)]
            else:
                d[num] = i


pprint(Solution().twoSum(nums, target))
