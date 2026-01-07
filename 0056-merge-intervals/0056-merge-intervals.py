class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i=0
        intervals.sort()
        for j in range(len(intervals)):
            if intervals[i][1]>=intervals[j][0]:
                intervals[i][1]=max(intervals[i][1],intervals[j][1])
            else:
                i+=1
                intervals[i]=intervals[j]
        
        return intervals[:i+1]