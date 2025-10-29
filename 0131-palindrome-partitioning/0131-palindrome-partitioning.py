class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        def isPalindrome(st):
            return st==st[::-1]
        def backtrack(start,path):
            if start==len(s):
                res.append(path[:])
                return
            
            for i in range(start,len(s)):
                subS=s[start:i+1]
                if isPalindrome(subS):
                    path.append(subS)
                    backtrack(i+1,path)
                    path.pop()
        
        backtrack(0,[])
        return res