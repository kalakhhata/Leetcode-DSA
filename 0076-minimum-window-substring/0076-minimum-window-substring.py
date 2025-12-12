class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need=Counter(t)
        required=len(need)
        have=0
        l=0
        res=[-1,-1]
        max_len=float('inf')
        window={}
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in need and window[c]==need[c]:
                have+=1
            
            while have==required:
                
                if r-l+1<max_len:
                    max_len=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in need and window[s[l]]<need[s[l]]:
                    have-=1
                
                l+=1
        
        l,r=res
        return s[l:r+1] if max_len != float("inf") else ""
