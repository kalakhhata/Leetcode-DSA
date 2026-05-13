import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap=[]
        for point in points:
            x=point[0]**2
            y=point[1]**2
            heapq.heappush(maxHeap,(-(x+y),[point[0],point[1]]))
        
        while len(maxHeap)>k:
            heapq.heappop(maxHeap)
        
        return [point for key,point in maxHeap]
        

        