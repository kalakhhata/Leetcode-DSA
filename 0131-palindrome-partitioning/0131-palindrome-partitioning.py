class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(t):
            return t==t[::-1]
        res=[]
        ans=[]
        def dfs(start):
            if start==len(s):
                res.append(ans[:])
                return
            
            for end in range(start,len(s)):
                if isPalindrome(s[start:end+1]):
                    ans.append(s[start:end+1])
                    dfs(end+1)
                    ans.pop()
        
        dfs(0)
        return res


        