class Solution:
    def isValid(self, s: str) -> bool:
        
        st=[]
        bucket={')':'(',']':'[','}':'{'}
        cnt=0
        for p in s:
            if p in bucket:
                cnt-=1
                if not st or st.pop()!=bucket[p]:
                    return False
            else:
                st.append(p)
                cnt+=1
        return cnt==0
            
        
        