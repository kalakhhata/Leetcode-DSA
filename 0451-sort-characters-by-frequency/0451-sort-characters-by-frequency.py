class Solution:
    def frequencySort(self, s: str) -> str:
        #stores char:count in dict
        freq=Counter(s)
       
        #create a buckets to store char in terms of there count
        max_freq=max(freq.values())
        buckets=[[] for _ in range(max_freq+1)]

        #put the char in bucket in terms for their count
        for char,f in freq.items():
            buckets[f].append(char)
        
        #put the most frequent to least frequen char in res array
        res=[]
        for f in range(max_freq,0,-1):
            for char in buckets[f]:
                res.append(char*f)
        
        return ''.join(res)

        