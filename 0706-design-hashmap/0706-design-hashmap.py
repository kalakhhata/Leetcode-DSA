class MyHashMap:

    def __init__(self):
        self.size=1009
        self.bucket=[[] for _ in range(self.size)]
    
    def _hash(self,key):
        return key%self.size
        

    def put(self, key: int, value: int) -> None:
        h=self._hash(key)
        b=self.bucket[h]

        for i,(k,v) in enumerate(b):
            if k==key:
                b[i]=(k,value)
                return
        b.append((key,value))
        

    def get(self, key: int) -> int:
        h=self._hash(key)
        b=self.bucket[h]

        for i,(k,v) in enumerate(b):
            if k==key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        h=self._hash(key)
        b=self.bucket[h]

        for i,(k,v) in enumerate(b):
            if k==key:
                b.pop(i)
                return
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)