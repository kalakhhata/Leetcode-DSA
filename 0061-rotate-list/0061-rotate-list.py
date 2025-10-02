# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
        
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
        
        tail.next=head
        k=k%length
        steps=length-k
        tail_new=head
        for _ in range(steps-1):
            tail_new=tail_new.next
        new_head=tail_new.next
        tail_new.next=None

        return new_head
