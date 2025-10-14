class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        ans=[]
        def findCombination(i,target):
            if i==len(candidates):
                if target==0:
                    res.append(ans[:])
                return
            if candidates[i]<=target:
                ans.append(candidates[i])
                findCombination(i,target-candidates[i])

                ans.pop()
            findCombination(i+1,target)



        findCombination(0,target)
        return res