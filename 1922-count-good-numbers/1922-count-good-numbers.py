class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD=(10**9)+7
        even=(n+1)//2
        odd=n//2
        return (self.powC(5,even)*self.powC(4,odd))%MOD
    
    def powC(self,x,n):
        MOD=(10**9)+7
        if n==0:
            return 1
        half=self.powC(x,n//2)
        if n%2==0:
            return (half*half)%MOD
        else:
            return (half*half*x)%MOD
        