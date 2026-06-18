class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        comb=[]
        candidates.sort()

        def getComb(idx,comb,target):
            if target==0:
                res.append(comb[:])
                return
            
            if target<0:
                return
            
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i-1]==candidates[i]:
                    continue
                
                if target<candidates[i]:
                    break
                
                comb.append(candidates[i])
                getComb(i+1,comb,target-candidates[i])
                comb.pop()
        
        getComb(0,comb,target)
        return res