"""
Output list so that output[i] is the product of all elements in array except itself i. 

Notes:
* No division allowed 
* Must be O(n)
"""

# Input
nums = [1, 2, 3, 4]
output = [24, 12, 8, 6]

############ Initial Answer (n) ########
_sum = []
place_holder = 1
for i in range(0, len(nums)):
    _sum.append(place_holder)
    place_holder *= nums[i]

# [1,1,2,6]
# Sum all of the elements on the right of ith element
place_holder = 1
for i in range(len(nums) - 1, -1, -1):
    _sum[i] *= place_holder
    place_holder *= nums[i]
#######################################

############ Using two pointers (n) ########
"""
Thought this solution might be faster in time complexity,
but it wasn't...
"""
if len(nums) <= 1:
    print([0])

left, right = 0, len(nums) - 1
left_sum, right_sum = 1, 1
_sums = [1] * len(nums)

while left < len(nums) - 1 and right > 0:
    left_sum *= nums[left]
    right_sum *= nums[right]
    left += 1
    right -= 1
    _sums[left] *= left_sum
    _sums[right] *= right_sum

print(_sums)
############################################
