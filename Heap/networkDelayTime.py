# Use Dijkstra' Algorithm to find the shortest path from K to all nodes
# Based on heap implemention, time is O(ElogE). Space is O(N+E) because the size of graph
# is O(E) and the the overall distance is N.
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        g = collections.defaultdict(list)
        for u, v, w in times:
            g[u].append((v,w))
        heap = [(0, K)]
        dist = {}
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for v, w in g[node]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        return max(dist.values()) if len(dist) == N else -1
