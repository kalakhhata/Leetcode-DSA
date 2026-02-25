# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        
        target=l//2
        pivot=target-1

        temp=0
        curr=head
        while curr:
            if temp==pivot:
                curr.next=curr.next.next if curr.next else None
                break
            temp+=1
            curr=curr.next
        
        return head


        