class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        #max and min
        IMAX=2**31-1
        IMIN=-2**31
        num=0
        #takes care of the whitespace
        s=s.lstrip()
        if not s:
            return 0
        
        #takes care of sign or unsign
        sign=1
        if s[0] in ['+','-']:
            if s[0]=='-':
                sign=-1
            s=s[1:]
        
        #now it Read the integer by skipping leading zeros until a non-digit character is encountered
        n=self.getNum(s,0,0)
        
        #sign coversion
        n*=sign
        if n>IMAX:
            return IMAX
        if n<IMIN:
            return IMIN
        
        return n
    
    def getNum(self,s,i,num):

        #base-case
        if i>=len(s) or not s[i].isdigit():
            return num
        
        num=(num*10) + int(s[i])
        return self.getNum(s,i+1,num)



        