"""
Return two index with two values that sums up to the target number
Time Complexity: O(n)

Notes:
"""

# Input
nums = [2, 7, 11, 15]
target = 9

################################################
dic = {}

for i, num in enumerate(nums):
    if target - num in dic:
        print([i, dic[target - num]])
    else:
        dic[num] = i
################################################
