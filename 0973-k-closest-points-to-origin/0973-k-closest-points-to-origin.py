class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:


        heap=[]
        q=deque()
        for point in points:
            a=point[0]**2
            b=point[1]**2
            heapq.heappush(heap,(-(a+b),[point[0],point[1]]))

        while len(heap)>k:
            heapq.heappop(heap)
        
        return [point for key,point in heap]

        