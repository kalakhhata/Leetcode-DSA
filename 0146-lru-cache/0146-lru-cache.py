class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #here we store the capacity of db ll
        self.cap=capacity
        #we use a dictionoary so we can store key-value (key-Node) pair for O(1) retrival
        self.cache={}
        #we use dummy nodes left and right that takes care of lru and mru node's info
        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    
    def insert(self,node):
        prev=self.right.prev
        next=self.right
        node.next=next
        node.prev=prev
        prev.next=node
        next.prev=node
    



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
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)