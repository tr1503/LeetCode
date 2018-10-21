class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # for each building 1, run bfs and return for each 0
        n = len(grid)
        m = len(grid[0])
        buildings = sum(grid[x][y] for x in range(n) for y in range(m) if grid[x][y] == 1)
        distance = collections.defaultdict(list)
        def bfs(iStart, jStart):
            queue = [(iStart, jStart, 0)]
            visited = [[False for _ in range(m)] for _ in range(n)]
            visited[iStart][jStart] = True
            count = 0
            while queue:
                i, j, dist = queue.pop()
                # bfs bruning: visit points with 1 but not put in queue
                # check out at end, make sure it goes to all buildings
                for x, y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                        visited[x][y] = True
                        if grid[x][y] == 0:
                            distance[(x,y)].append(dist + 1)
                            queue.insert(0, (x, y, dist + 1))
                        elif grid[x][y] == 1:
                            count += 1
            return count == buildings - 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if not bfs(i,j):
                        return -1
        res = float('inf')
        for (i,j), distances in distance.items():
            if len(distances) == buildings:
                res = min(res, sum(distances))
        return -1 if res == float('inf') else res
