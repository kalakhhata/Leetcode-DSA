class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)
        i=0
        heap=[]
        for key in freq:
            heapq.heappush(heap,(-freq[key],key))
        ans=''
        prev=None
        while heap:
            cnt,char=heapq.heappop(heap)
            cnt+=1
            ans+=char
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            
            if cnt<0:
                prev=(cnt,char)
        if prev:
            return ''
        return ans


        