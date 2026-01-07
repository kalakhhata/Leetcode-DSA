class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        i=0
        cnt=0

        for j in range(1,len(intervals)):
            if intervals[i][1]>intervals[j][0]:
                cnt+=1
                intervals[i][1]=min(intervals[i][1],intervals[j][1])
            else:
                i+=1
                intervals[i]=intervals[j]
        
        return cnt