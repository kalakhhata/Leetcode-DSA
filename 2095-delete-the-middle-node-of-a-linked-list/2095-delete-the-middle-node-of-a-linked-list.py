# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        curr=head
        cnt=0
        while curr:
            curr=curr.next
            cnt+=1
        pivot=cnt//2
        curr=head

        for i in range(pivot-1):
            curr=curr.next
        
        curr.next=curr.next.next if curr.next else None

        return head