# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        #Sort the intervals based on the start value.
        intervals.sort(key = lambda x:x.start)
        merged = []
        for interval in intervals:
            #If the start is smaller than the last interval's end, it is not overlapped.
            #Add to result intervals.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            #If the start is larger than the last interval's end, it is overlapped.
            #Change the last end to the larger number between this interval's end and last interval's end.
            else:
                merged[-1].end = max(merged[-1].end,interval.end)
        return merged
