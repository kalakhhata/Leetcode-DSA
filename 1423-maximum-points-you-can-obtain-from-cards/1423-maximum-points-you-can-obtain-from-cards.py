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
        lindex=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[lindex]
            lindex-=1
            maxSum=max(maxSum,lsum+rsum)
        
        return maxSum

        