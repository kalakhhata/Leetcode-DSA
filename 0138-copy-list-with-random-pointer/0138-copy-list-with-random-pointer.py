"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        curr=head
        while curr:
            dummy=Node(curr.val)
            dummy.next=curr.next
            curr.next=dummy
            curr=curr.next.next
        
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            else:
                curr.next.random=curr.random
            curr=curr.next.next
        
        curr=head
        n=Node(-1)
        dummy=n
        while curr:
            dummy.next=curr.next
            dummy=dummy.next
            curr.next=dummy.next
            curr=curr.next
        return n.next

