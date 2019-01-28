class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0
        m = len(picture)
        n = len(picture[0])
        res = 0
        rowCount = [0 for _ in range(m)]
        colCount = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rowCount[i] += 1
                    colCount[j] += 1
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if rowCount[i] == 1 and colCount[j] == 1:
                        res += 1
        return res
