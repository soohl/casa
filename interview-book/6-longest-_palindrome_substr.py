# class Solution:
#     def longestPalindrome(self, s: str) -> str:

if len(s) < 2 or s == s[::-1]:
    print(s)

result = ""
len_s = len(s)


def expand(left, right):
    while left >= 0 and right < len_s and (s[left] == s[right]):
        left -= 1
        right += 1

    return s[left + 1 : right]


for i in range(len_s - 1):

    result = max(
        result,
        expand(i, i + 1),
        expand(i, i + 2),
        key=len,
    )

print(result)
