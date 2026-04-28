# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the middle element
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #half reverse the list
        prev=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        #merge the linkedlist as required
        left=head
        right=prev
        while right.next:
            tmp=left.next
            left.next=right
            left=tmp

            tmp=right.next
            right.next=left
            right=tmp
            
        
