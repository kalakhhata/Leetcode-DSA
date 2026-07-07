class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        rev=digits[::-1]
        carry=1
        i=0

        while i<len(digits) and carry!=0:
            if rev[i]<9:
                rev[i]+=1
                return rev[::-1]
            rev[i]=0
            i+=1
        rev.append(1)
        return rev[::-1]
            


        