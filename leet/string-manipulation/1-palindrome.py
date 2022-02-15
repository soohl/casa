"""
Check if a given string is a palindrome

Time Complexity: O(n)

Notes:
isalnum() = returns true if all char in the string are alphanumeric
"""

# Input
s = "A man, a plan, a canal: Panama"
# Output
o = True

#######################################
new_str = [c.lower() for c in s if c.isalnum()]
print(new_str[:] == new_str[::-1])
#######################################
