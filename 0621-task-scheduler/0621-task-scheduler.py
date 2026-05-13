import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxHeap=[]
        for key in freq:
            heapq.heappush(maxHeap,-freq[key])
        cnt=0
        q=deque()
        i=0

        while maxHeap or q:
            
            if maxHeap:
                t=-heapq.heappop(maxHeap)-1
                if t!=0:
                    q.append([t,n+i])
            if q and q[0][1]==i:
                t1,_=q.popleft()
                heapq.heappush(maxHeap,-t1)
            i+=1
            
        return i



        