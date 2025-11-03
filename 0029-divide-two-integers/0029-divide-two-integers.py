class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX=2**31-1
        INT_MIN=-2**31

        if dividend==INT_MIN and divisor==-1:
            return INT_MAX
        
        negative = (dividend<0)!=(divisor<0)

        dividend=abs(dividend)
        divisor=abs(divisor)
        
        quotint=0
        while dividend>=divisor:
            temp=divisor
            multiply=1
            while dividend>=(temp<<1):
                temp=temp<<1
                multiply=multiply<<1
            dividend-=temp
            quotint+=multiply
        
        if negative:
            quotint=-quotint
        
        return max(min(quotint,INT_MAX),INT_MIN)

        