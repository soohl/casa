"""
Print the longest palindrome

Time Complexity: O(n)

Notes:
Using two pointers expanding from the middle 
"""

# Input
s = "babad"

############## Using a two pointer ###################
def expand(left, right):
    while left >= 0 and right < len(s) and (s[left] == s[right]):
        left -= 1
        right += 1
    return s[left + 1 : right]


if len(s) < 2 or s == s[::-1]:
    # In this case, we don't need to expand in the first place
    print(s)
else:
    result = ""
    for i in range(len(s) - 1):
        result = max(
            result,
            expand(i, i + 1),  # 짝수로 expand
            expand(i, i + 2),  # 홀수로 expand
            key=len,
        )

    print(result)
###############################################
