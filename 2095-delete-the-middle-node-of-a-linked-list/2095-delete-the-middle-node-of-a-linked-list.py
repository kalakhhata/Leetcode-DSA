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
        curr=head
        cnt=0
        while curr:
            cnt+=1
            curr=curr.next

        m=(cnt//2)
        if m==0:
            return None
        curr=head
        for i in range(cnt):
            if i==m-1:
                break
            curr=curr.next
        
        curr.next = curr.next.next if curr.next else None

        return head