import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap=[]
        for num in nums:
            heapq.heappush(minheap,num)
            if len(minheap)>k:
                heapq.heappop(minheap)
        
        return minheap[0]