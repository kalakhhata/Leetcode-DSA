class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st=[]
        ans=[0]*len(temperatures)

        for i,val in enumerate(temperatures):
            while st and temperatures[st[-1]]<val:
                idx=st.pop()
                ans[idx]=i-idx
            st.append(i)
        
        return ans

        