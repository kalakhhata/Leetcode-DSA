class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        bucket=defaultdict(int)
        for c1,c2 in zip(s,t):
            bucket[c1]+=1
            bucket[c2]-=1
        
        for key in bucket:
            if bucket[key]!=0:
                return False
        
        return True

        