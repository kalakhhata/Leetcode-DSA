class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l=0
        r=len(s)-1
        vs=set(['a','e','i','o','u'])

        while l<r:
            if s[l].lower() not in vs:
                l+=1
            elif s[r].lower() not in vs:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return ''.join(s)
            
        