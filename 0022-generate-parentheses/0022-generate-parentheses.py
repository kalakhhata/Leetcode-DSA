class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(l,r,s):
            if l==r==0:
                res.append(s)
                return
            
            if l>0:
                backtrack(l-1,r,s+'(')
            if r>l:
                backtrack(l,r-1,s+')')
        
        res=[]
        backtrack(n,n,'')
        return res



        