class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums2)
        stack=[]
        nge=defaultdict(lambda:-1)

        for num in nums2:
            while stack and stack[-1]<num:
                nge[stack.pop()]=num
            stack.append(num)
        
        return [nge[num] for num in nums1]