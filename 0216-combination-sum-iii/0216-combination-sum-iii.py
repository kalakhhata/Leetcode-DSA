class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr=[1,2,3,4,5,6,7,8,9]
        ans=[]
        res=[]

        def getCombination(i,temp):
            if temp==n and len(ans)==k:
                res.append(ans[:])
                return
            
            if i>=len(arr) or temp>n:
                return
            
            ans.append(arr[i])
            getCombination(i+1,temp+arr[i])
            ans.pop()

            getCombination(i+1,temp)
        
        getCombination(0,0)
        return res
