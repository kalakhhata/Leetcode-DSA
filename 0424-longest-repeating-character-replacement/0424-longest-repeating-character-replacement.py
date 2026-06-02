class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26
        left=0
        max_freq=0
        ans=0

        for r in range(len(s)):
            freq[ord(s[r])-ord('A')]+=1
            max_freq=max(max_freq,freq[ord(s[r])-ord('A')])

            if (r-left+1)-max_freq>k:
                freq[ord(s[left])-ord('A')]-=1
                left+=1
            ans=max(ans,r-left+1)
        return ans

        