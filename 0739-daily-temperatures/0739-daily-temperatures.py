class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]

        for curr_day,temp in enumerate(temperatures):

            while st and temperatures[st[-1]]<temp:
                prev_day=st.pop()
                ans[prev_day]=curr_day-prev_day
            st.append(curr_day)
        
        return ans
        
        