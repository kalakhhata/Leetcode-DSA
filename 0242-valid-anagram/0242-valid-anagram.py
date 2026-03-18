class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        bucket=[0]*26

        for c1,c2 in zip(s,t):
            bucket[ord(c1)-ord('a')]+=1
            bucket[ord(c2)-ord('a')]-=1
        
        for i in range(len(bucket)):
            if bucket[i]!=0:
                return False
        return True


        