"""
Input is the level of elevation. Calculate how much rain water can be trapped.

Time Complexity: O(n)

Notes:
"""

# Input
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = 6

############### INITIAL ANSWER (n^2) ####################
if not height:
    print(0)

water = 0
for f in range(1, max(height) + 1):
    flag = False
    flag_index = 0
    for i in range(len(height)):
        if height[i] >= f:
            if not flag:
                flag = True
                flag_index = i
            else:
                water += i - flag_index - 1
                flag_index = i
                flag = True

print(water)
################################################

######### TWO POINTERS TO MAX (n) ##############
if not height:
    print(0)

volume = 0
left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]

while left < right:
    left_max, right_max = max(height[left], left_max), max(
        height[right], right_max
    )
    if left_max <= right_max:
        volume += left_max - height[left]
        left += 1
    else:
        volume += right_max - height[right]
        right -= 1

print(volume)
################################################

######### STACK (n) ##############
stack = []
volume = 0

for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
        top = stack.pop()

        if not stack:
            break

        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]]) - height[top]
        volume += distance * waters

    stack.append(i)

print(volume)
################################################
