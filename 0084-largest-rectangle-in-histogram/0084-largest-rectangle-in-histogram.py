class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxEl=0
        st=[]
        n=len(heights)

        for i in range(n):
            while st and heights[st[-1]]>heights[i]:
                el=heights[st.pop()]
                nle=i
                ple=st[-1] if st else -1
                maxEl=max(maxEl,el*(nle-ple-1))
            st.append(i)
        
        while st:
            el=heights[st.pop()]
            nle=n
            ple=st[-1] if st else -1
            maxEl=max(maxEl,el*(nle-ple-1))
        
        return maxEl

            
                
