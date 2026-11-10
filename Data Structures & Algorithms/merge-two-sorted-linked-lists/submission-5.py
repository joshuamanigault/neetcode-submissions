# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d_head = ListNode()
        c = d_head
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next

        if l2:
            while l2:
                c.next = l2
                l2 = l2.next
                c = c.next
        else:
            while l1:
                c.next = l1
                l1 = l1.next
                c = c.next
        return d_head.next


        