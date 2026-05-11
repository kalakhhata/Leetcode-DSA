import heapq
class MedianFinder:

    def __init__(self):
        self.left_heap=[]
        self.right_heap=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap,-num)

        if self.left_heap and self.right_heap and -self.left_heap[0]>self.right_heap[0]:
            heapq.heappush(self.right_heap,-heapq.heappop(self.left_heap))
        
        if len(self.right_heap)>len(self.left_heap)+1:
            heapq.heappush(self.left_heap,-heapq.heappop(self.right_heap))
        
        if len(self.left_heap)>len(self.right_heap)+1:
            heapq.heappush(self.right_heap,-heapq.heappop(self.left_heap))



        

    def findMedian(self) -> float:
        if len(self.right_heap)>len(self.left_heap):
            return float(self.right_heap[0])
        
        if len(self.left_heap)>len(self.right_heap):
            return float(-self.left_heap[0])
        
        return (self.right_heap[0]-self.left_heap[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()