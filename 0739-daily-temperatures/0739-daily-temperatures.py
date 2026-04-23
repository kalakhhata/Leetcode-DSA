class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st=[]
        ans=[0]*len(temperatures)

        for curr_day,curr_temp in enumerate(temperatures):
            while st and temperatures[st[-1]]<curr_temp:
                prev_day=st.pop()
                ans[prev_day]=curr_day-prev_day
            st.append(curr_day)
        
        return ans
        