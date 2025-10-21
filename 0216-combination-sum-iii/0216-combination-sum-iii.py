class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        num=[1,2,3,4,5,6,7,8,9]
        res=[]
        ans=[]
        def getCombination(i,temp):
            if temp==0 and len(ans)==k:
                res.append(ans[:])
                return
            
            if i==len(num) or num[i]>temp:
                return
            
            
            
            #pick
            ans.append(num[i])
            getCombination(i+1,temp-num[i])
            #not-pick
            ans.pop()
            getCombination(i+1,temp)
        
        getCombination(0,n)
        return res