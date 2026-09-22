class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap=[]
        for stone in stones:
            heapq.heappush(self.heap,-stone)
        
        while len(self.heap)>1:
            s1=-heapq.heappop(self.heap)
            s2=-heapq.heappop(self.heap)

            if s2<s1:
                heapq.heappush(self.heap,-(s1-s2))
        return -self.heap[0] if self.heap else 0


        