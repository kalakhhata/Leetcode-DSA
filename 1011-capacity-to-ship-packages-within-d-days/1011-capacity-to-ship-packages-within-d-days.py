class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=low+(high-low)//2
            if self.canShip(weights,days,mid):
                high=mid-1
            else:
                low=mid+1
        
        return low
    
    def canShip(self,weights,days,mid):
        day=1
        cnt=weights[0]
        for i in range(1,len(weights)):
            if cnt+weights[i]<=mid:
                cnt+=weights[i]
            else:
                day+=1
                cnt=weights[i]
        return day<=days


            
        