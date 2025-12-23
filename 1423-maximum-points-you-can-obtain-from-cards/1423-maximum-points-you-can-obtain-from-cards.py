class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        lsum=sum(cardPoints[:k])
        rsum=0
        maxSum=lsum
        rindex=len(cardPoints)-1

        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            rindex-=1
            maxSum=max(maxSum,rsum+lsum)
        
        return maxSum