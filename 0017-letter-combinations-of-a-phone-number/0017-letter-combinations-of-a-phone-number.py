class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        if len(digits)==0:
            return res
        pad={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def getLetter(idx,comb):
            if idx==len(digits):
                res.append(comb[:])
                return

            for letter in pad[digits[idx]]:
                getLetter(idx+1,comb+letter)
        
        getLetter(0,'')

        return res
                


        