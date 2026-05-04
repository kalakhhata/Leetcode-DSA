# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        dummy=ans
        l1=list1
        l2=list2

        while l1 or l2:
            val1=l1.val if l1 else float('inf')
            val2=l2.val if l2 else float('inf')

            if val1<=val2:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        
        return ans.next
        

            
        