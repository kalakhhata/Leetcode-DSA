class Node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.nxt=None
        self.prev=None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.nxt=self.right
        self.right.prev=self.left

    
    def remove(self,node):
        prev=node.prev
        nxt=node.nxt
        prev.nxt=nxt
        nxt.prev=prev
    
    def insert(self,node):
        prev=self.right.prev
        nxt=self.right
        node.nxt=nxt
        nxt.prev=node
        node.prev=prev
        prev.nxt=node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)