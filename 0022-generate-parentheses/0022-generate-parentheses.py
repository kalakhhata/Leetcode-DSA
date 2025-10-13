class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def generate(open,close,s):
            if open==0 and close==0:
                res.append(s)
                return
            
            if open>0:
                generate(open-1,close,s+'(')
            
            if close>open:
                generate(open,close-1,s+')')
        
        generate(n,n,'')
        return res
        