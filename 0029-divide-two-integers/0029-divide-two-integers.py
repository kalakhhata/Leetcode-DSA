class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX=2**31-1
        INT_MIN=-2**31

        #one and only overflow condition
        if dividend==INT_MIN and divisor==-1:
            return INT_MAX
        
        #check if any of the value is negative. if both the value is positive or negative it will remain false
        #only when one of them is negative it will be true
        negative = (dividend<0) != (divisor<0)

        #covert it to its absolute value
        dividend=abs(dividend)
        divisor=abs(divisor)
        
        # ex. 10/3 = 3 <- That is quotint
        quotint=0
        
        #This while loop will run till dividend<divisor
        while dividend>=divisor:
            temp=divisor
            multiply=1
            while dividend>=temp<<1:  # 1)10>=6 2)10>=12 #1)4>=6
                temp=temp<<1 #6 
                multiply=multiply<<1 #2
            dividend-=temp #4 #1
            quotint+=multiply #2 #3
        
        if negative:
            quotint=-quotint
        
        return max(min(quotint,INT_MAX),INT_MIN)
            

