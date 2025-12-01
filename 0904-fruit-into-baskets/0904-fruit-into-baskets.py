class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        ans=0
        fruit_count=defaultdict(int)

        for right in range(len(fruits)):
            fruit_count[fruits[right]]+=1

            while len(fruit_count)>2:
                fruit_count[fruits[left]]-=1
                if fruit_count[fruits[left]]==0:
                    del fruit_count[fruits[left]]
                left+=1

            ans=max(ans,right-left+1)
        
        return ans