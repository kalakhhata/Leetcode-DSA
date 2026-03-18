class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=0
        bucket=defaultdict(int)

        for i in range(len(nums)):
            if target-nums[i] in bucket:
                return [i,bucket[target-nums[i]]]
            bucket[nums[i]]=i
        return [-1,-1]
        