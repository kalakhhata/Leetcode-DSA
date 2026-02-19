class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref=strs[0]
        pref_len=len(pref)

        for i in range(1,len(strs)):
            s=strs[i]
            while s[:pref_len]!=pref[:pref_len] and pref_len!=0:
                pref_len-=1
        
        return pref[:pref_len]
