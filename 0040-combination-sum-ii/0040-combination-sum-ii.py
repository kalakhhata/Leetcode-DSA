class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        sub=[]
        candidates.sort()
        def findSubset(start,target):
            if target<0:
                return
            if target==0:
                res.append(sub[:])
                return
            
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                sub.append(candidates[i])
                findSubset(i+1,target-candidates[i])
                sub.pop()
        findSubset(0,target)
        return res
        