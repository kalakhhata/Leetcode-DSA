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
        hash = {None:None}
        curr=head
        
        while curr:
            hash[curr]=Node(curr.val)
            curr=curr.next
            

        curr=head
        while curr:
            copyNode=hash[curr]
            copyNode.next=hash[curr.next]
            copyNode.random=hash[curr.random]
            curr=curr.next
        return hash[head]