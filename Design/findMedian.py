class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap,-num)
            return
        
        if len(self.maxHeap) == len(self.minHeap):
            if -num > self.maxHeap[0]:
                heapq.heappush(self.maxHeap,-num)
            else:
                heapq.heappush(self.minHeap,num)
        
        elif len(self.maxHeap) > len(self.minHeap):
            if -num < self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.minHeap, -self.maxHeap[0])
                heapq.heapreplace(self.maxHeap, -num)
                
        elif len(self.maxHeap) < len(self.minHeap):
            if num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.maxHeap, -self.minHeap[0])
                heapq.heapreplace(self.minHeap,num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        elif len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return float(self.minHeap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()