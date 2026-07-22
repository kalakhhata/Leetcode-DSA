class Solution:
    def isValid(self, s: str) -> bool:
        hm={')':'(',']':'[','}':'{'}
        st=[]

        for c in s:
            if c in hm.values():
                st.append(c)
            elif not st or st.pop()!=hm[c]:
                return False
        return not st
        