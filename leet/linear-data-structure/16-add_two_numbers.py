"""
Add Numbers stored as reverse linked list
Notes:
* divmod() : takes 2 numbers and returns a pair of numbers (a tuple) consisting their quotient and remainder
* WILL NOT RUN ON LOCAL AS LINKED LIST IS NOT DEFINED

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Input = (2->4->3) + (5->6->4)
# Output = 7->0->8
# 342 + 465 = 807

############ Initial Answer O(n) ########
root = head = ListNode(0)

carry = 0
while l1 or l2 or carry:
    sum = 0
    if l1:
        sum += l1.val
        l1 = l1.next
    if l2:
        sum += l2.val
        l2 = l2.next

    carry, val = divmod(sum + carry, 10)
    head.next = ListNode(val)
    head = head.next

print(root.next)
############################################
