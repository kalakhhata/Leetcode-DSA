# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        curr=head
        cnt=0
        while curr:
            cnt+=1
            curr=curr.next
            
        pivot=cnt-n
        if pivot==0:
            return head.next
        curr=head
        cnt=0
        while curr:
            cnt+=1
            if cnt==pivot:
                curr.next=curr.next.next
                break
            curr=curr.next
        

            
        return head