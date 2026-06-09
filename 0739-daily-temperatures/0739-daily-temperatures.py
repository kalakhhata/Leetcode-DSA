class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:



        ans=[0]*len(temperatures)
        st=[]
        for i,val in enumerate(temperatures):
            while st and temperatures[st[-1]]<val:
                idx=st.pop()
                ans[idx]=i-idx
            st.append(i)
        
        return ans
            
        