class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.res = []
        i = 0
        j = 0
        while i < len(v1) and j < len(v2):
            self.res.append(v1[i])
            self.res.append(v2[j])
            i += 1
            j += 1
        while i < len(v1):
            self.res.append(v1[i])
            i += 1
        while j < len(v2):
            self.res.append(v2[j])
            j += 1
        self.index = -1
        
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:
            self.index += 1
            return self.res[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index + 1 < len(self.res)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
