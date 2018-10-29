class Solution: 
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # dfs method, time is O(e + q * e), space is O(e)
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
        
        # union find method, time is O(e + q), space is O(e), e is equation, q is queries.
        # each query uses O(1) time
        def find(x):
            if x != parent[x][0]:
                px, pv = find(parent[x][0])
                parent[x] = (px, parent[x][1] * pv)
            return parent[x]
        def divide(x,y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry:
                return -1.0
            return vx / vy
        parent = {}
        res = []
        for (x,y), v in zip(equations, values):
            if x not in parent and y not in parent:
                parent[x] = (y, v)
                parent[y] = (y, 1.0)
            elif x not in parent:
                parent[x] = (y, v)
            elif y not in parent:
                parent[y] = (x, 1.0 / v)
            else:
                rx, vx = find(x)
                ry, vy = find(y)
                parent[rx] = (ry, v / vx * vy)
        for x, y in queries:
            if x in parent and y in parent:
                res.append(divide(x,y))
            else:
                res.append(-1.0)
        return res
