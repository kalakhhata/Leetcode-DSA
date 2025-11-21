class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def getArea(height):
            stack=[]
            maxA=0
            n=len(height)

            for i in range(n):
                while stack and height[stack[-1]]>height[i]:
                    el=height[stack.pop()]
                    nle=i
                    ple=stack[-1] if stack else -1
                    maxA=max(maxA,el*(nle-ple-1))
                stack.append(i)
            
            while stack:
                el=height[stack.pop()]
                nle=n
                ple=stack[-1] if stack else -1
                maxA = max(maxA,el*(nle-ple-1))
            
            return maxA
        
        n=len(matrix[0])
        height=[0]*n
        maxArea=0

        for row in matrix:
            for i in range(n):
                if row[i]=='1':
                    height[i]+=1
                else:
                    height[i]=0
            maxArea=max(maxArea,getArea(height))
        
        return maxArea
        