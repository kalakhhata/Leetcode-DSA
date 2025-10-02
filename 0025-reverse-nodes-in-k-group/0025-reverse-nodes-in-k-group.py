# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        cnt=0
        temp=head
        while temp and cnt<k:
            temp=temp.next
            cnt+=1
        
        if cnt<k:
            return head
        
        prev=None
        curr=head
        for _ in range(k):
            face=curr.next
            curr.next=prev
            prev=curr
            curr=face
        
        head.next=self.reverseKGroup(curr,k)

        return prev
        