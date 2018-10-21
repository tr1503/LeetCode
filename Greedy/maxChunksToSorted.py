class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        m = 0
        for i, n in enumerate(arr):
            if n > m:
                m = n
            if m == i:
                res += 1
        return res
