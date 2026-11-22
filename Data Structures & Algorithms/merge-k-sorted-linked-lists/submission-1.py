# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        dummy_head = ListNode(0)
        curr = dummy_head

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        
        return dummy_head.next