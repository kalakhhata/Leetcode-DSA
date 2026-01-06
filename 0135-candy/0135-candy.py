class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        candies=n
        i=1

        while i<n:
            if ratings[i-1]==ratings[i]:
                i+=1
                continue
            
            peak=0
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                candies+=peak
                i+=1
            
            vally=0
            while i<n and ratings[i]<ratings[i-1]:
                vally+=1
                candies+=vally
                i+=1
            
            candies-=min(peak,vally)
        
        return candies