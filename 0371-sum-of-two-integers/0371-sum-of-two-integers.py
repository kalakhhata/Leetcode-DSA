class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask=0xffffffff

        while b&mask>0:
            a,b=a^b,(a&b)<<1
        
        return (mask&a) if b>0 else a