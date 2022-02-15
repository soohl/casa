"""
Use n pair of min(a,b) to get highest sum

Time Complexity: Best is O(n^2)?

Notes:
"""

# Input
nums = [1, 4, 3, 2]  # 2n integers group
output = 4  # min(1,2) + min(3,4) = 4

############ Initial Answer (n) ########
result = 0
nums.sort()
for i in range(0, len(nums), 2):
    result += min(nums[i], nums[i + 1])
print(result)

########### Only even position num (n) ####################
result = sum(sorted(nums[::2]))
print(result)
