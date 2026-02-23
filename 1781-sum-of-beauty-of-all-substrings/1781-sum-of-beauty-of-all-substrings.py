class Solution:
    def beautySum(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            freq={}
            for j in range(i,len(s)):
                freq[s[j]] = freq.get(s[j],0)+1
                beauty = self.getMax(freq)-self.getMin(freq)
                sum+=beauty
        
        return sum
    
    def getMax(self,freq)->int:
        maxi=0
        for count in freq.values():
            maxi=max(maxi,count)
        return maxi
    
    def getMin(self,freq)->int:
        mini=float("inf")
        for count in freq.values():
            mini=min(mini,count)
        return mini


        