'''Use dfs to do this question. Details: https://leetcode.com/problems/redundant-connection-ii/solution/'''
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parents = {}
        candidates = []
        for u, v in edges:
            if v in parents:
                candidates.append((parents[v],v))
                candidates.append((u,v))
            else:
                parents[v] = u
        def orbit(node):
            visited = set()
            while node in parents and node not in visited:
                visited.add(node)
                node = parents[node]
            return node, visited
        
        root = orbit(1)[0]
        if not candidates:
            cycle = orbit(root)[1]
            for u,v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans
        
        children = collections.defaultdict(list)
        for v in parents:
            children[parents[v]].append(v)
            
        visited = [True] + [False] * n
        stack = [root]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                stack.extend(children[node])
        return candidates[all(visited)]
