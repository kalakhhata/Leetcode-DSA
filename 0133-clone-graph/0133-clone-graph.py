"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hm={}
        def clone(node):
            if node in hm:
                return hm[node]
            
            copyN=Node(node.val)
            hm[node]=copyN

            for ne in node.neighbors:
                copyN.neighbors.append(clone(ne))
            return copyN
        
        return clone(node)

        