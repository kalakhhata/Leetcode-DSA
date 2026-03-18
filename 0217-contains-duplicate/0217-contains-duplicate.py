class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bucket=set()
        for num in nums:
            if num in bucket:
                return True
            bucket.add(num)
        return False


        