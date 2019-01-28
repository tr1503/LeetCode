# Convert this question to numbers of islands, the result is the numbers of stones - the numbers of islands
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        for i, j in stones:
            rows[i].add(j)
            cols[j].add(i)
        
        def dfsRow(i):
            R.add(i)
            for j in rows[i]:
                if j not in C:
                    dfsCol(j)
        def dfsCol(j):
            C.add(j)
            for i in cols[j]:
                if i not in R:
                    dfsRow(i)
        R, C = set(), set()
        islands = 0
        for i, j in stones:
            if i not in R:
                islands += 1
                dfsRow(i)
                dfsCol(j)
        return len(stones) - islands
