class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map={}
        for sc,tc in zip(s,t):
            if sc in char_map:
                if char_map[sc]!=tc:
                    return False
            elif tc in char_map.values():
                return False
            char_map[sc]=tc
        return True
        

        