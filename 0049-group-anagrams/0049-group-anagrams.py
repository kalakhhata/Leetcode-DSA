class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket=defaultdict(list)

        for st in strs:
            count=[0]*26

            for c in st:
                count[ord(c)-ord('a')]+=1
            bucket[tuple(count)].append(st)
        
        return list(bucket.values())

        