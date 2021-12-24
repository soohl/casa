# class Solution:
#     def isPalindrome(self, s: str) -> bool:

s = "A man, a plan, a canal: Panama"
new_strs: list = [c.lower() for c in s if c.isalnum()]

print(new_strs, new_strs[:] == new_strs[::-1])
