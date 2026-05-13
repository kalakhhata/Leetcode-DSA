import heapq
class MedianFinder:

    def __init__(self):
        self.left=[] #max-heap
        self.right=[] #min-heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)

        if self.right and -self.left[0]>self.right[0]:
            heapq.heappush(self.right,-heapq.heappop(self.left))


        if len(self.right)+1<len(self.left):
            heapq.heappush(self.right,-heapq.heappop(self.left))
        
        if len(self.left)+1<len(self.right)+1:
            heapq.heappush(self.left,-heapq.heappop(self.right))
        



        

    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            return (self.right[0]-self.left[0])/2
        elif len(self.left)>len(self.right):
            return -float(self.left[0])
        else:
            return float(self.right[0])
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()