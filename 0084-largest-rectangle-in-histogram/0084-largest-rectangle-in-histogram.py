class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea=0
        st=[]
        for i in range(len(heights)):
            while st and heights[st[-1]]>heights[i]:
                el=heights[st.pop()]
                nle=i
                ple=st[-1] if st else -1
                maxArea=max(maxArea,el*(nle-ple-1))
            st.append(i)
        
        while st:
            el=heights[st.pop()]
            nle=len(heights)
            ple=st[-1] if st else -1
            maxArea=max(maxArea,el*(nle-ple-1))
        return maxArea