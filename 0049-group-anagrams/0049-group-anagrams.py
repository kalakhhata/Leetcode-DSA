class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for st in strs:
            bucket=[0]*26
            
            for c in st:
                bucket[ord(c)-ord('a')]+=1
            ans[tuple(bucket)].append(st)
        
        return list(ans.values())
