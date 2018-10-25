# use bfs to search from the boundary to the extrances of two oceans
# if both of them get to oceans, then they should be the result
class Solution:
    dirs = [[0,-1],[0,1],[-1,0],[1,0]]
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        p = set()
        a = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    p.add((i,j))
                if i == m - 1 or j == n - 1:
                    a.add((i,j))
        def bfs(curr, ocean):
            while curr:
                nxt = set()
                for i, j in curr:
                    for x, y in self.dirs:
                        nx = i + x
                        ny = j + y
                        if nx < 0 or ny < 0 or nx >= m or ny >= n:
                            continue
                        neigh = (nx, ny)
                        if neigh in curr or neigh in ocean or matrix[i][j] > matrix[nx][ny]:
                            continue
                        nxt.add(neigh)
                        ocean.add(neigh)
                curr = nxt
        currP = set(p)
        currA = set(a)
        bfs(currP,p)
        bfs(currA,a)
        return list(p&a)
