# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        slow=head
        fast=head.next
        rem=head.next
        while fast and fast.next:
            slow.next=fast.next
            slow=slow.next
            fast.next=slow.next
            fast=fast.next
        slow.next=rem
        return head