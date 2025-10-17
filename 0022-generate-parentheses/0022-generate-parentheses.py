class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def getParentheses(l,r,st):
            #base-case
            if l==r==0:
                res.append(st)
                return
            if l>0:
                getParentheses(l-1,r,st+'(')
            if r>0 and r>l:
                getParentheses(l,r-1,st+')')
        
        getParentheses(n,n,'')
        return res
