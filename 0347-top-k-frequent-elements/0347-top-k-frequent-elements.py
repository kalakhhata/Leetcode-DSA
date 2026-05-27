class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for i in range(len(nums)+1)]
        for idx,val in count.items():
            freq[val].append(idx)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            
            if len(res)==k:
                return res


        
        