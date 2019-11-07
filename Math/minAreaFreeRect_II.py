class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        d = collections.defaultdict(list)
        for i in range(n - 1):
            pi = points[i]
            for j in range(i + 1, n):
                pj = points[j]
                line = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2
                x = (pi[0] + pj[0]) / 2.0
                y = (pi[1] + pj[1]) / 2.0
                d[(line, x, y)].append((i, j))
        res = float('inf')
        for line in d.values():
            m = len(line)
            for i in range(m - 1):
                p0 = points[line[i][0]]
                p2 = points[line[i][1]]
                for j in range(i + 1, m):
                    p1 = points[line[j][0]]
                    p3 = points[line[j][1]]
                    diagonal1 = math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)
                    diagonal2 = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                    area = diagonal1 * diagonal2
                    res = min(res, area)
        return 0 if res == float('inf') else res
