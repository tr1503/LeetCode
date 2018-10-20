# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x.start)
        end = intervals[0].end
        prev = 0
        count = 0
        for i in range(1,len(intervals)):
            if intervals[prev].end > intervals[i].start:
                if intervals[prev].end > intervals[i].end:
                    prev = i
                count += 1
            else:
                prev = i
        return count
