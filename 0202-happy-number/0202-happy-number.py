class Solution:
    def isHappy(self, n: int) -> bool:

        seen=set()

        while n not in seen:
            seen.add(n)
            n=self.numOfSquares(n)
            if n==1:
                return True
        return False
        
        


    def numOfSquares(self,n):
        output=0

        while n:
            digits=n%10
            digits=digits**2
            n=n//10
            output+=digits
        return output


        