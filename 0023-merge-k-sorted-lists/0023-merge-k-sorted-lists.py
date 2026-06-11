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
        min_heap=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val,i,node))
        ans=ListNode()
        dummy=ans
        while min_heap:
            val,idx,node=heapq.heappop(min_heap)
            dummy.next=node
            dummy=dummy.next
            if node.next:
                heapq.heappush(min_heap,(node.next.val,i+1,node.next))
        
        return ans.next

        