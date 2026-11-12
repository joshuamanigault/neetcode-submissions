# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        heap = []
        for head in lists:
            curr = head
            while curr:
                heap.append(curr.val)
                curr = curr.next
        
        heapq.heapify(heap)
        dummy_head = ListNode(0)
        curr = dummy_head

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        

        return dummy_head.next
        