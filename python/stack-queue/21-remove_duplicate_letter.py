"""
Exclude duplicates alphabet and order in lexicographical order

Notes:
"""

# Input = bcabc
# Output = abc

############ Using a stack O(n) ########
s = 'bcabc'
import collections
from unittest.mock import sentinel
counter, seen, stack = collections.Counter(s), set(), []

for c in s:
    counter[c] -= 1
    if c in seen:
        continue
    # 현재 문자가 쌓여있고, 뒤에 다시 붙일 문자가 남아있다면 스택에서 꺼내서 없앤다.
    while stack and c < stack[-1] and counter[stack[-1]] > 0:
        seen.remove(stack.pop())
    stack.append(c)
    seen.add(c)

print(''.join(stack))
########################################
