import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[]
        for stone in stones:
            maxHeap.append(-stone)
        heapq.heapify(maxHeap)

        for i in range(len(stones)-1):
            el1=-heapq.heappop(maxHeap)
            el2=-heapq.heappop(maxHeap)
            if el1-el2==0:
                heapq.heappush(maxHeap,0)
            else:
                heapq.heappush(maxHeap,-(el1-el2))
        
        return -maxHeap[0]

        