"""
Output whether the singly linked list is palindrome

Notes:
* WILL NOT RUN ON LOCAL AS LINKED LIST IS NOT DEFINED

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Input = 1->2
# Output = false

############ Initial Answer O(n) ########
nodes = []

while head:
    nodes.append(head.val)
    head = head.next

print(nodes == nodes[::-1])
#######################################

############ Use deque O(n) ########
from collections import deque

nodes = deque()

while head:
    nodes.append(head.val)
    head = head.next

while nodes:
    if nodes.pop() != nodes.popleft():
        print(False)
        break
print(True)
#######################################

############ Use Runner O(n) #######
rev = None
slow = fast = head

while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next

# when there are odd # of nodes, we need to move slow to the next node
# to skip the middle element
if fast:
    slow = slow.next

while rev and rev.val == slow.val:
    rev, slow = rev.next, slow.next

print(not rev)
#######################################
