class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_t=Counter(t)
        need=len(dict_t)
        have=0
        max_len=float('inf')
        res=[-1,-1]
        l=0
        window=defaultdict(int)

        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1

            if c in dict_t and window[c]==dict_t[c]:
                have+=1
            
            while have==need:
                if r-l+1<max_len:
                    max_len=r-l+1
                    res[0]=l
                    res[1]=r
                
                window[s[l]]-=1
                if s[l] in dict_t and window[s[l]]<dict_t[s[l]]:
                    have-=1
                l+=1
        
        l,r=res

        return s[l:r+1] if max_len!=float('inf') else ''
                