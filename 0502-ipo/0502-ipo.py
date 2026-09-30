class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n=len(profits)
        projects=list(zip(capital,profits))
        projects.sort()
        heap=[]
        i=0
        for _ in range(k):
            while i<n and projects[i][0]<=w:
                heappush(heap,-projects[i][1])
                i+=1
            if not heap:
                break
            w+=-heappop(heap)
        return w
