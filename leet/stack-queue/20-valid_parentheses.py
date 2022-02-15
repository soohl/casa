"""
Check if the parenthesis are valid

Notes:
"""

# Input = ()[]{}
# Output = true

# ([])
# [([]{})]
#

s = "()[]{}"
############ Using a stack O(n) ########
stack = []

key = [")", "}", "]"]
value = ["(", "{", "["]
mapping_table = dict(zip(key, value))

for c in s:
    if c not in mapping_table:
        stack.append(c)
    else:
        if not stack or mapping_table[c] != stack.pop():
            print(False)
            break

print(not any(stack))
########################################
