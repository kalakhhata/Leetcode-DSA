class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        for i in range(32):
            bit=(n>>i)&1
            ans=ans<<1 | bit
        return ans

