class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        lCount = 0
        rCount = 0
        for i in range(len(start)):
            if start[i] == 'R':
                rCount += 1
            if end[i] == 'L':
                lCount += 1
            if start[i] == 'L':
                lCount -= 1
            if end[i] == 'R':
                rCount -= 1
            if lCount < 0 or rCount < 0 or lCount * rCount != 0:
                return False
        return lCount == 0 and rCount == 0
