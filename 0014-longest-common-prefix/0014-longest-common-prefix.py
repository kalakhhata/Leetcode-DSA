class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        ans=strs[0]
        for i,s in enumerate(strs):
            j=0
            while j<len(ans) and j<len(s) and s[j]==ans[j]:
                j+=1
            ans=ans[:j]
        return ans
            


        