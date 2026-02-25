# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        
        pivot=(l-n)-1
        if pivot==-1:
            return head.next
        temp=0
        curr=head
        while curr:
            
            if temp==pivot:
                curr.next=curr.next.next if curr.next else None
                break
            temp+=1
            curr=curr.next
        return head


        