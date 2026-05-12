class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        subset=[]
        ans=[]

        def findCombination(i,target,subset):
            if i==len(candidates):
                if target==0:
                    ans.append(subset[:])
                return
            
            if target>=candidates[i]:
                subset.append(candidates[i])
                findCombination(i,target-candidates[i],subset)
                subset.pop()
            findCombination(i+1,target,subset)
        
        findCombination(0,target,subset)
        return ans
                    
        