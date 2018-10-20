class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        m = {}
        #Use hashmap to build a stop -> buses, like one stop has some buses stop at here.
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop in m:
                    m[stop].append(i)
                else:
                    m[stop] = []
                    m[stop].append(i)
        visited = [0 for _ in range(len(routes))]
        queue = []
        queue.append(S)
        buses = 0
        while len(queue) != 0:
            size = len(queue)
            buses += 1
            for i in range(size):
                curr = queue.pop(0)
                for bus in m[curr]:
                    if visited[bus] == 1:
                        continue
                    visited[bus] = 1
                    for stop in routes[bus]:
                        if stop == T:
                            return buses
                        queue.append(stop)
        return -1
