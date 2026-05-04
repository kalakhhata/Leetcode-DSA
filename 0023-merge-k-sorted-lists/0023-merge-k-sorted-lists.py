import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap=[]
        ans=ListNode()
        dummy=ans

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(minheap,(node.val,i,node))
        
        while minheap:
            val,idx,node=heapq.heappop(minheap)
            dummy.next=ListNode(val)
            dummy=dummy.next
            if node.next:
                heapq.heappush(minheap,(node.next.val,idx+1,node.next))
        
        return ans.next


        