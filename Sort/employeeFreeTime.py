# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        start = 0
        end = 1
        events = []
        # Extract the intervals from schedule
        for s in schedule:
            for interval in s:
                events.append((interval.start, start))
                events.append((interval.end, end))
        events.sort()
        
        # Merge intervals
        res = []
        balance = 0
        prev = None
        for t, event in events:
            if balance == 0 and prev is not None:
                res.append(Interval(prev, t))
            balance += 1 if event == start else -1
            if balance == 0:
                prev = t
        return res
