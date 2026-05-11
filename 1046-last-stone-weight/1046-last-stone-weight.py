import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            el1=-heapq.heappop(heap)
            el2=-heapq.heappop(heap)
            if el1==el2:
                continue
            el=el1-el2
            heapq.heappush(heap,-el)
        
        return -heap[0] if heap else 0


        
        