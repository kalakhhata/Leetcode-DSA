class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:

        heap=[]
        res=[]
        i=0
        tasks = [[en, pr, idx] for idx, (en, pr) in enumerate(tasks)]
        tasks.sort()
        time=0
        
        
        while heap or i<len(tasks):

            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))
                i+=1
            if not heap:
                time=tasks[i][0]
                continue
            
            pr,idx=heapq.heappop(heap)
            res.append(idx)
            time+=pr
        return res
            
        