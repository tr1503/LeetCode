class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = [0]*(len(edges) + 1)
        s = [1]*(len(edges) + 1)
        
        def find(u):
            while p[u] != u:
                p[u] = p[p[u]]
                u = p[u]
            return u
        
        for u, v in edges:
            if p[u] == 0: p[u] = u
            if p[v] == 0: p[v] = v
            pu, pv = find(u), find(v)
            if pu == pv: return [u, v]
            
            if s[pv] > s[pu]: u, v = v, u
            p[pv] = pu
            s[pu] += s[pv]
 
        return []
