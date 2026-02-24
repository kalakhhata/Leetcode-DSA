# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getNode(self,head,fast):
        if head==fast:
            return fast
        return self.getNode(head.next,fast.next)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                node=self.getNode(head,fast)
                return node
        
        return None

        