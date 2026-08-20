# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]

        def build(root):
            if not root:
                res.append('N')
                return
            
            res.append(str(root.val))
            build(root.left)
            build(root.right)
        
        build(root)
        return ','.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        self.i=0
        nodeVal=data.split(',')

        def construct():
            val=nodeVal[self.i]
            self.i+=1

            if val=='N':
                return None
            
            node=TreeNode(int(val))
            node.left=construct()
            node.right=construct()
            return node
        
        return construct()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))