class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]

        for digit in num:
            while stack and k>0 and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        
        #if k>0
        stack=stack[:-k] if k else stack

        #remove leading 0
        result = ''.join(stack).lstrip('0')

        #make sure result is not empty str
        return result if result else '0'


        