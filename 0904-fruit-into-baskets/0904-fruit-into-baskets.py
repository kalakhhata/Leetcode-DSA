class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        basket=0
        ans=0
        basket=defaultdict(int)

        for right in range(len(fruits)):
            basket[fruits[right]]+=1

            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1
                
            ans=max(ans,right-left+1)
        
        return ans

