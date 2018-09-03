class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.list = []
        self.sum = 0
        self.capacity = size
        self.size = 0
        self.flag = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size < self.capacity:
            self.list.append(val)
            self.size += 1.0
            self.sum += val
            return self.sum / self.size
        else:
            self.sum -= self.list[self.flag]
            self.flag += 1
            self.list.append(val)
            self.sum += val
            return self.sum / self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)