# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        freeRoom = []
        #Sort intervals by start time
        intervals.sort(key = lambda x:x.start)
        #Create a heap for free room, push the end time
        heapq.heappush(freeRoom,intervals[0].end)
        for i in range(1,len(intervals)):
            #Find the room that can be used because this time interval can start on time
            if freeRoom[0] <= intervals[i].start:
                heapq.heappop(freeRoom)
            #Push the interval's end time to heap
            heapq.heappush(freeRoom,intervals[i].end)
        return len(freeRoom)
