class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        subset=[]
        res=[]

        def getSubset(i,target,subset):
            if i==len(candidates):
                if target==0:
                    res.append(subset[:])
                return
            
            if target>=candidates[i]:
                subset.append(candidates[i])
                getSubset(i,target-candidates[i],subset)
                subset.pop()
            getSubset(i+1,target,subset)
        
        getSubset(0,target,subset)
        return res
        