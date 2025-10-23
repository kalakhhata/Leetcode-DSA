class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]

        def getSubset(start,path):
            if len(s)==start:
                res.append(path[:])
                return
            
            for i in range(start,len(s)):
                subS=s[start:i+1]
                if isPalindrome(subS):
                    path.append(subS)
                    getSubset(i+1,path)
                    path.pop()

        
        def isPalindrome(st):
            l=0
            r=len(st)-1
            while l<=r:
                if st[l]!=st[r]:
                    return False
                l+=1
                r-=1
            return True
        
        getSubset(0,[])
        return res