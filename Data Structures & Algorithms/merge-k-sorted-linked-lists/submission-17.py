# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(minHeap, (lst.val, i, lst))
        
        dummy = curr = ListNode()
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return dummy.next