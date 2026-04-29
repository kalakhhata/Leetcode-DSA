# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem=0
        s1=l1
        s2=l2
        ans=ListNode(-1)
        dummy=ans

        while s1 or s2 or rem!=0:
            num1=s1.val if s1 else 0
            num2=s2.val if s2 else 0
            s=num1+num2+rem
            q=s%10
            node=ListNode(q)
            dummy.next=node
            dummy=dummy.next
            rem=s//10
            s1=s1.next if s1 else None
            s2=s2.next if s2 else None
        return ans.next

            