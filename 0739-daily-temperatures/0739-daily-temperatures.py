class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st=[]
        ans=[0]*len(temperatures)

        for curr_day,temp in enumerate(temperatures):
            while st and temperatures[st[-1]]<temp:
                prev_day=st.pop()
                days=curr_day-prev_day
                ans[prev_day]=days
            st.append(curr_day)
        return ans

        