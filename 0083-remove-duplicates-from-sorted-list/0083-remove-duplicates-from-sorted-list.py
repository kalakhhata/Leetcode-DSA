# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        prev=head
        curr=head.next
        while curr:
            if prev.val==curr.val:
                prev.next=curr.next if curr.next else None
            else:
                prev=curr
            curr=curr.next
        return head