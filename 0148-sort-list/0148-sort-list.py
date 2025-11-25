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
        if not head or not head.next:
            return head
        
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.sortList(head)
        right=self.sortList(mid)

        return self.getSorted(left,right)
    
    def getSorted(self,left,right):
        dummyNode=ListNode(-1)
        temp=dummyNode
        while left and right:
            if left.val<=right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next
        temp.next=left if left else right
        return dummyNode.next


        