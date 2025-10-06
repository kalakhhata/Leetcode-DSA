# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #base-case
        if not head or not head.next:
            return head
        
        #find the mid
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #handle the last nodes correctly
        mid=slow.next
        slow.next=None

        #split both halves
        left=self.sortList(head)
        right=self.sortList(mid)

        return self.merge(left,right)
    
    def merge(self,left,right):
        dummy = ListNode()
        ansLL=dummy

        while left and right:
            if left.val<=right.val:
                ansLL.next=left
                left=left.next
            else:
                ansLL.next=right
                right=right.next
            ansLL=ansLL.next
        
        ansLL.next=left if left else right
        
        return dummy.next