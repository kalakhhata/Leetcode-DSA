class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX_INT=2**31-1
        MIN_INT=-2**31
        s=s.lstrip()
        if not s:
            return 0
        
        sign=1
        if s[0] in ['+','-']:
            if s[0]=='-':
                sign=-1
            s=s[1:]
        num=self.helper(0,0,s)
        if num*sign>MAX_INT:
            return MAX_INT
        elif num*sign<MIN_INT:
            return MIN_INT
        return num*sign
    
    def helper(self,num,i,s):
        

        if i>=len(s) or not s[i].isdigit():
            return num
        
        num=num*10+int(s[i])

        return self.helper(num,i+1,s)