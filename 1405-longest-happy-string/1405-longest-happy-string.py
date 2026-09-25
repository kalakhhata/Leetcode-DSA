class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        prev=None
        freq=0
        heap=[]
        for cnt, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if cnt > 0:
                heapq.heappush(heap, (-cnt, ch))
        
            

        res=''

        while heap:
            cnt,ch=heapq.heappop(heap)
            if len(res)>=2 and res[-1]==res[-2]==ch:
                if not heap:
                    break
                cnt2,ch2=heapq.heappop(heap)
                
                res+=ch2
                cnt2+=1
                if cnt2!=0:
                    heapq.heappush(heap,(cnt2,ch2))
                heapq.heappush(heap,(cnt,ch))
            else:

                
                cnt+=1
                res+=ch
                if cnt!=0:
                    heapq.heappush(heap,(cnt,ch))
                
            
        return res

            

        