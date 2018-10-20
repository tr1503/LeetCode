class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        LA = [(xi, yi) for xi in range(n) for yi in range(n) if A[xi][yi]]
        LB = [(xi, yi) for xi in range(n) for yi in range(n) if B[xi][yi]]
        dic = collections.Counter([(x1-x2, y1-y2) for (x1,y1) in LA for (x2,y2) in LB])
        return max(dic.values() or [0])
