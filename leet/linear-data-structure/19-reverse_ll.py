"""
Make reverse linked list from index m to index n (m starts from 1)
Notes:

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Input = 1->2->3->4->5->NULL, m=2, n=4
# Output = 1->4->3->2->5>NULL

############ Initial Answer O(n) ########
if not head or m == n:
    return head

root = start = ListNode(None)
root.next = head

for _ in range(m - 1):
    start = start.next
end = start.next

for _ in range(n - m):
    tmp, start.next, end.next = start.next, end.next, end.next.next
    start.next.next = tmp

return root.next
########################################
