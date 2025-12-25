import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        cool_down=deque()
        time=0

        while max_heap or cool_down:
            time+=1

            if max_heap:
                cnt=heapq.heappop(max_heap)+1
                if cnt!=0:
                    cool_down.append((cnt,time+n))
            
            if cool_down and cool_down[0][1]==time:
                heapq.heappush(max_heap,cool_down.popleft()[0])
        
        return time
        