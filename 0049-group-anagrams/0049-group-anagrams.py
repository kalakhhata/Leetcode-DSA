class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        bucket=defaultdict(list)
    
        for st in strs:
            freq=[0]*26

            for s in st:
                freq[ord(s)-ord('a')]+=1
            bucket[tuple(freq)].append(st)
        
        return [bucket[key] for key in bucket]

        