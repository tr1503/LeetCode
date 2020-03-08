class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(p) for p in blocked}
        
        def bfs(source, target):
            arr = [source]
            visited = {tuple(source)}
            for x0, y0 in arr:
                for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
                    x = x0 + i
                    y = y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in visited and (x, y) not in blocked:
                        if [x, y] == target:
                            return True
                        arr.append([x, y])
                        visited.add((x, y))
                if len(arr) == 20000:
                    return True
            return False
        return bfs(source, target) and bfs(target, source)
