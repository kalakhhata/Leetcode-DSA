import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        minheap=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(minheap,(node.val,i,node))
        
        dummyNode = ListNode(0)
        tempIdx = dummyNode

        while minheap:
            val,i,node=heapq.heappop(minheap)
            tempIdx.next=node
            tempIdx=tempIdx.next

            if node.next:
                heapq.heappush(minheap,(node.next.val,i,node.next))
        
        return dummyNode.next
        