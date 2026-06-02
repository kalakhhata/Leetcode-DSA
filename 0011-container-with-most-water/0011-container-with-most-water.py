class Solution:
    def maxArea(self, height: List[int]) -> int:
        k=0
        l=len(height)-1
        ans=0

        while k<l:
            hi=min(height[k],height[l])
            width=(l-k)
            ans=max(ans,hi*width)
            if height[k]<=height[l]:
                k+=1
            else:
                l-=1
        return ans
