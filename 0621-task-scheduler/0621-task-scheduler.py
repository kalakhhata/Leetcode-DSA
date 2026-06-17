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

        while max_heap or q:
            if max_heap:
                t=-heapq.heappop(max_heap)-1
                if t!=0:
                    q.append([-t,i+n])
            
            if q and q[0][1]==i:
                rt,_=q.popleft()
                heapq.heappush(max_heap,rt)
            i+=1
        return i
        