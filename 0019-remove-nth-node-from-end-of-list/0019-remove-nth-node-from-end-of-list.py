# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0
        curr=head
        while curr:
            cnt+=1
            curr=curr.next
        if cnt==n:
            return head.next
        targetIdx=cnt-n

        curr=head
        prev=None
        idx=0
        while curr:
            idx+=1
            prev=curr
            curr=curr.next
            if idx==targetIdx:
                prev.next=curr.next if curr else None
        return head
        