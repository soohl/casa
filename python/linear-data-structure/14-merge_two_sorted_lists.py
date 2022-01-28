"""
Merge two sorted linked list

Notes:
* WILL NOT RUN ON LOCAL AS LINKED LIST IS NOT DEFINED

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Input = 1->2->4, 1->3->4
# Output = 1->1->2->3->4->4

############ Initial Answer O(n) ########
############ Initial Answer O(n) ########
result = ListNode()
head = result

while list1 or list2:

    head.next = ListNode()
    head = head.next

    if not list1:
        head.val, list2 = list2.val, list2.next
        continue

    if not list2:
        head.val, list1 = list1.val, list1.next
        continue

    if list1.val < list2.val:
        head.val, list1 = list1.val, list1.next
    else:
        head.val, list2 = list2.val, list2.next

print(result.next)
###########################################

############ Recursive Answer O(n) ######## ???????????????
if (not list1) or (list2 and list1.val > list2.val):
    list1, list2 = list2, list1

if list1:
    list1.next = self.mergeTwoLists(list1.next, list2)

print(list1)
############################################
