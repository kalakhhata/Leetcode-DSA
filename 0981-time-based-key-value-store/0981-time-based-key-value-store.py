class TimeMap(object):

    def __init__(self):
        self.bucket=defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.bucket[key].append((value,timestamp))
        return None
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res=''
        if key not in self.bucket:
            return ''
        else:
            l=0
            r=len(self.bucket[key])-1
            while l<=r:
                mid=l+(r-l)//2
               
                if self.bucket[key][mid][1]>timestamp:
                    r=mid-1
                else:
                    res=self.bucket[key][mid][0]
                    l=mid+1
    
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)