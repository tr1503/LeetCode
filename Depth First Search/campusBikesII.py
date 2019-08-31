# Use dfs with memory by bit records to solve this problem
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        def calculate(i, visited, cache):
            if i == len(workers):
                return 0
            if (i, visited) in cache:
                return cache[(i, visited)]
            
            res = float('inf')
            for j, bike in enumerate(bikes):
                if visited & 1 << j: 
                    continue;
                res = min(res, dist(bike, workers[i]) + calculate(i + 1, visited | 1 << j, cache))
            cache[(i, visited)] = res
            return res
        return calculate(0, 0, {})
