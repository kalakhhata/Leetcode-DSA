class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        bucket=defaultdict(int)
        bucket={0:1}
        total=0
        cnt=0
        for num in nums:
            total+=num
            
            rem=total-k
            if rem in bucket:
                cnt+=bucket[rem]
            bucket[total]=bucket.get(total,0)+1
        return cnt

        
        