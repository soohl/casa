"""
Alter the linked list so that even nodes comes after all the odd nodes. 
Time complexity must be O(n) with O(1) space complexity

Notes:

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Input = 1->2->3->4->5->NULL
# Output = 1->3->5->2->4->NULL

############ Initial Answer O(n) ########
if not head:
    return head

odd = head
even = head.next
even_head = head.next

while even and even.next:
    odd.next = odd.next.next
    odd = odd.next
    even.next = even.next.next
    even = even.next

odd.next = even_head
return head
##############################################
