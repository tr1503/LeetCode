class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)
        
        jump = [-1 for _ in range(n)]
        def dfs(v, parent, level, jump, res, g):
            jump[v] = level + 1
            
            for child in g[v]:
                if child == parent:
                    continue
                elif jump[child] == -1:
                    jump[v] = min(jump[v], dfs(child, v, level + 1, jump, res, g))
                else:
                    jump[v] = min(jump[v], jump[child])
            
            if jump[v] == level + 1 and v != 0:
                res.append([parent, v])
            
            return jump[v]
        
        res = []
        dfs(0, -1, 0, jump, res, g)
        return res
