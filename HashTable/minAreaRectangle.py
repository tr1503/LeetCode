# Convert question to 4 sum II based on diagonal line. Time is O(n^2), space is O(n)
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = map(tuple, points)
        points.sort()
        s = set(points)
        n = len(points)
        res = float('inf')
        for i in range(n - 1):
            p1 = points[i]
            for j in range(i + 1, n):
                p4 = points[j]
                if p4[0] == p1[0] or p4[1] == p1[1]:
                    continue
                p2 = (p1[0], p4[1])
                p3 = (p4[0], p1[1])
                if p2 in s and p3 in s:
                    res = min(res, abs(p3[0] - p1[0]) * abs(p2[1] - p1[1]))
        return res if res != float('inf') else 0
