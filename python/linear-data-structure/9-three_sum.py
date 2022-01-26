"""
Find possible 3 elements that sums up to 0 
Time Complexity: Best is O(n^2)?

Notes:
"""

# Input
from typing import DefaultDict


nums = [-1, 0, 1, 2, -1, -4]
output = [[-1, 0, 1], [-1, -1, 2]]
############### TWO-POINTER ANSWER (n^2) ####################

nums.sort()
result = []

for i in range(len(nums) - 2):

    # 중복 값은 비교를 뛰어넘는다.
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left, right = i + 1, len(nums) - 1

    while left < right:
        sum_of_three = nums[i] + nums[left] + nums[right]

        if sum_of_three < 0:
            left += 1
        elif sum_of_three > 0:
            right -= 1
        else:
            # when sum == 0
            result.append([nums[i], nums[left], nums[right]])

            # 중복값 스킵
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1
            right -= 1

print(result)
################################################
