class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
        for key in d:
            d[key].sort(reverse = True)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i-j].pop()
        return mat
