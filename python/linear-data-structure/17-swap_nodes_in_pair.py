"""
Swap nodes in pair

Notes:

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Input = 1->2->3->4
# Output = 2->1->3->4

############ Initial Answer O(n) ########
if not head or not head.next:
    print(head)
first, second = head, head.next

while second:
    first.val, second.val = second.val, first.val

    if not second.next:
        break

    first, second = first.next.next, second.next.next

print(head)
############################################

############ Other answer ########
curr = head

while curr:
    curr.val, curr.next.val = curr.next.val, curr.val
    curr = curr.next.next

print(head)
############################################

############ Other answer ########
root = prev = ListNode(None)

prev.next = head
while head and head.next:
    b = head.next
    head.next = b.next
    b.next = head

    prev.next = b

    head = head.next
    prev = prev.next.next

print(root.next)
############################################

############ Recursive answer ########
if head and head.next:
    p = head.next
    head.next = self.swapPairs(p.next)
    p.next = head
    return p
return head
############################################
