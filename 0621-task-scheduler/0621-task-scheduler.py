import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        max_heap=[]
        for key in freq:
            heapq.heappush(max_heap,-freq[key])
        
        q=deque()
        i=0

        while q or max_heap:
            if max_heap:
                t=-heapq.heappop(max_heap)-1
                if t!=0:
                    q.append([t,i+n])
            
            if q and q[0][1]==i:
                t1,_=q.popleft()
                heapq.heappush(max_heap,-t1)
            i+=1
        
        return i


        