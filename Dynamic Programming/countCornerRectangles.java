class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [[c for c, val in enumerate(row) if val] for row in grid]
        n = sum(sum(row) for row in grid)
        root = int(math.sqrt(n))
        
        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= root:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= root:
                        continue
                    found = 0
                    for c2 in row2:
                        if c2 in target:
                            found += 1
                    ans += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1
        return int(ans)
                    
