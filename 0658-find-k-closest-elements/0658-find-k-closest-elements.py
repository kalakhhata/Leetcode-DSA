class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        dis_list=[abs(n-x) for n in arr]
        mini=minsum=sum(dis_list[:k])
        idx=0

        for i in range(1,len(arr)-k+1):
            minsum=minsum+arr[i+k-1]-arr[i-1]
            if minsum<mini:
                mini=minsum
                idx=i
        
        return arr[idx:idx+k]
        