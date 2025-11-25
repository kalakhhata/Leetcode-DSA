class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        q=deque()

        for idx,num in enumerate(nums):
            #firstly we run while loop to check if deque has elements and last element is smaller than the current el we pop out the element to keep the max value at top
            while q and q[-1]<num:
                q.pop()
            q.append(num)

            #not here we check if we are in next window we donts have the previos's window's max elment if so we pop out from front

            if idx>=k and nums[idx-k]==q[0]:
                q.popleft()
            #here we check we we have crossed k-1 element to make sure if window is generated we add the mac element in result which is at top
            if idx>=k-1:
                ans.append(q[0])
        
        return ans