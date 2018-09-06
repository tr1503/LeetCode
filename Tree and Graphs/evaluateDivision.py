class Solution: 
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(x, y, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for n in g[x]:
                if n in visited:
                    continue
                visited.add(n)
                ans = dfs(n, y, visited)
                if ans > 0:
                    return ans * g[x][n]
            return -1.0
        
        
        g = collections.defaultdict(dict)
        for (x,y), v in zip(equations, values):
            g[x][y] = v
            g[y][x] = 1.0 / v
        result = []
        for x,y in queries:
            if x in g and y in g:
                result.append(dfs(x,y,set()))
            else:
                result.append(-1.0)
        
        return result
