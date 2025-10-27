class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        ans=[]
        candidates.sort()
        def findC(idx,target):
            if target<0:
                return
            if target==0:
                res.append(ans[:])
                return
            
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if target<candidates[i]:
                    break
                
                ans.append(candidates[i])
                findC(i+1,target-candidates[i])
                ans.pop()
        
        findC(0,target)
        return res

        