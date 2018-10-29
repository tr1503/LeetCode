# get 8 neighbor's value and sum them // the number of them
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M or not M[0]:
            return []
        m = len(M)
        n = len(M[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
        for i in range(m):
            for j in range(n):
                count = M[i][j]
                t = 1
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    t += 1
                    count += M[x][y]
                res[i][j] = count // t
        return res
