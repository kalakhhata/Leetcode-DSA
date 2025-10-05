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
            copy=Node(curr.val)
            copy.next=curr.next
            curr.next=copy
            curr=curr.next.next
        
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            else:
                curr.next.random=curr.random
            curr=curr.next.next
        
        curr=head
        N=Node(-1)
        newN=N
        while curr:
            newN.next=curr.next
            newN=newN.next
            curr.next=newN.next
            curr=curr.next
        return N.next



        