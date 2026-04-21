class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        
        ss1=[0]*26
        ss2=[0]*26

        for i in range(len(s1)):
            ss1[ord(s1[i]) - ord('a')] += 1
            ss2[ord(s2[i]) - ord('a')] += 1
        
        if ss1==ss2:
            return True
        
        left=0
        for right in range(len(s1),len(s2)):
            ss2[ord(s2[right])-ord('a')]+=1
            ss2[ord(s2[left])-ord('a')]-=1
            left+=1
            if ss1==ss2:
                return True
        
        return False