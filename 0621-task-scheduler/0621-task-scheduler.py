class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        freq=Counter(tasks)
        heap=[]
        for key in freq:
            heapq.heappush(heap,-freq[key])
        q=deque()
        ans=0

        while heap or q:
            if len(heap)>0:
                cnt=-heapq.heappop(heap)
                cnt-=1
                if cnt>0:
                    q.append((cnt,ans+n))
            
            



            if len(q)>0 and q[0][1]==ans:
                cnt,ans=q.popleft()
                heapq.heappush(heap,-cnt)
            ans+=1
        return ans

            







        