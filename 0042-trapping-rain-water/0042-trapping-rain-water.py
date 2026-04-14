class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        lmax=height[left]
        rmax=height[right]
        res=0
        while left<right:
            if height[left]<height[right]:
                left+=1
                lmax=max(lmax,height[left])
                res+=lmax-height[left]
            else:
                right-=1
                rmax=max(rmax,height[right])
                res+=rmax-height[right]
        
        return res

        