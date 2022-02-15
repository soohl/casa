"""
Reverse the linked list

Notes:
* WILL NOT RUN ON LOCAL AS LINKED LIST IS NOT DEFINED

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Input = 1->2->3->4->5->NULL
# Output = 5->4->3->2->1->NULL

############ Initial Answer O(n) ########
result = None

while head:
    new_head = ListNode(val=head.val, next=result)
    result, head = new_head, head.next

print(result)
############################################

############ Second Iterative Answer O(n) ########
result, prev = head, None

while result:
    next, result.next = result.next, prev
    prev, result = result, next

print(result)
############################################

############ Recursive Answer O(n) ########
def reverse(node, prev=None):
    if not node:
        return prev
    next, node.next = node.next, prev
    return reverse(next, node)


print(reverse(head))
############################################
