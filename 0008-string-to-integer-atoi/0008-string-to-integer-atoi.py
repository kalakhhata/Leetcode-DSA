class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lstrip()
        if not s:
            return 0
        sign=1
        if s[0] in ['+','-']:
            if s[0]=='-':
                sign=-1
            s=s[1:]
        MIN=-2**31
        MAX=2**(31)-1
        num=self.getDigit(s,0,0)
        if sign==-1:
            num=num*-1
        if num<MIN:
            return MIN
        if num>MAX:
            return MAX
        
        return num

    def getDigit(self,s,i,n):
        if i>=len(s) or not s[i].isdigit():
            return n
        
        n=n*10+int(s[i])
        return self.getDigit(s,i+1,n)

         