class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        mid=-1
        while low<=high:
            mid=low+(high-low)//2
            if self.canEat(piles,mid,h):
                high=mid-1
            else:
                low=mid+1
        
        return low
    
    def canEat(self,piles,mid,h):
        cnt=0
        for pile in piles:
            cnt+=math.ceil(pile/mid)
        return cnt<=h
                