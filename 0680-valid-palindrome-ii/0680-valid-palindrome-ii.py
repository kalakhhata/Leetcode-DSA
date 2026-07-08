class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(i,j,s):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        i=0
        j=len(s)-1

        while i<j:
            if s[i]!=s[j]:
                return checkPalindrome(i+1,j,s) or checkPalindrome(i,j-1,s)
            i+=1
            j-=1
        return True
            

        