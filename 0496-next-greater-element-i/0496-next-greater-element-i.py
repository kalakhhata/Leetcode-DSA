class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ng=defaultdict(lambda : -1)
        stack=[]

        for num in nums2:
            while stack and stack[-1]<num:
                ng[stack.pop()]=num
            stack.append(num)
        
        return [ng[num] for num in nums1]
        


        