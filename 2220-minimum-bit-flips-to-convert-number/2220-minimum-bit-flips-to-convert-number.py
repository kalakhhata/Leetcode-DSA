class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        xor=start^goal
        
        cnt=0

        while xor:
            cnt+=xor & 1
            xor=xor>>1
        
        return cnt