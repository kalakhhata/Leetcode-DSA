class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        x,y=len(nums1),len(nums2)
        low=0
        high=x

        while low<=high:
            par1=(low+high)//2
            par2=((x+y+1)//2)-par1

            leftX=float('-inf') if par1==0 else nums1[par1-1]
            leftY=float('-inf') if par2==0 else nums2[par2-1]

            rightX=float('inf') if par1==x else nums1[par1]
            rightY=float('inf') if par2==y else nums2[par2]

            if leftX<=rightY and leftY<=rightX:
                if (x+y)%2==0:
                    return (max(leftX,leftY)+min(rightX,rightY))/2
                else:
                    return max(leftX,leftY)
            elif leftX>rightY:
                high=par1-1
            else:
                low=par1+1

        