class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif not stack or mapping[c]!=stack.pop():
                return False
        
        return not stack
            

        
        