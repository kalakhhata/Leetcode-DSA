class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        maxEl=0
        n=len(heights)

        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                el=heights[stack.pop()]
                nle=i
                ple=stack[-1] if stack else -1
                maxEl=max(maxEl,el*(nle-ple-1))
            stack.append(i)
        
        while stack:
            nle=n
            el=heights[stack.pop()]
            ple=stack[-1] if stack else -1
            maxEl=max(maxEl,el*(nle-ple-1))
        
        return maxEl