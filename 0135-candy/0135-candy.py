class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        candies=[1]*n


        #This loop will take care of left side distrubution
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        
        #This loop will take care of left and as well as right side distribution
        cnt=0
        for i in range(n-1,0,-1):
            if ratings[i-1]>ratings[i]:
                candies[i-1]=max(candies[i]+1,candies[i-1])
            cnt+=candies[i-1]
        
        return cnt+candies[n-1]
