class Solution:
    def isHappy(self, n: int) -> bool:

        
        slow=self.sumOf(n)
        fast=self.sumOf(self.sumOf(n))
        

        while fast!=1 and fast!=slow:
            slow=self.sumOf(slow)
            fast=self.sumOf(self.sumOf(fast))
        
        return fast==1
    
    def sumOf(self,n):
        total=0

        while n!=0:
            total+=(n%10)**2
            n=n//10
        return total