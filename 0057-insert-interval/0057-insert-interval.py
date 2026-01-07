class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()

        i=0
        for j in range(1,len(intervals)):
            if intervals[i][1]>=intervals[j][0]:
                intervals[i][1]=max(intervals[i][1],intervals[j][1])
            else:
                i+=1
                intervals[i]=intervals[j]
        
        return intervals[:i+1]
        