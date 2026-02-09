class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (m*k)>len(bloomDay):
            return -1
        
        low=min(bloomDay)
        high=max(bloomDay)

        while low<=high:
            mid=(low+high)//2
            ans=self.canBloom(bloomDay,m,k,mid)
            if ans:
                high=mid-1
            else:
                low=mid+1
        
        return low
    
    def canBloom(self,bloomDay,m,k,mid):
        bk=0
        flowers=0
        for day in bloomDay:
            if day<=mid:
                flowers+=1
            else:
                flowers=0
            
            if flowers==k:
                bk+=1
                flowers=0
        return bk>=m
            

        