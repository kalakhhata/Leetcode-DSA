class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if len(digits)==0:
            return res
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx,path):
            if idx==len(digits):
                res.append(path[:])
                return
            
            for letter in letters[digits[idx]]:
                backtrack(idx+1,path+letter)
        
        backtrack(0,'')
        return res