class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        minQ=deque()
        maxQ=deque()

        l=0
        ans=0

        for r in range(len(nums)):

            while minQ and nums[r]<minQ[-1]:
                minQ.pop()
            minQ.append(nums[r])

            while maxQ and nums[r]>maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[r])

            while maxQ[0]-minQ[0]>limit:
                if nums[l]==maxQ[0]:
                    maxQ.popleft()
                
                if nums[l]==minQ[0]:
                    minQ.popleft()
                l+=1
            ans=max(ans,r-l+1)
        
        return ans
        