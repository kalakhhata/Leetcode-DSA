class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        while n:
            n&=(n-1) #removes the lowest bit
            cnt+=1
        
        return cnt