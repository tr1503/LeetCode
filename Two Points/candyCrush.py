class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(board)
        n = len(board[0])
        #iter the board until the board stable
        #check each candy on the board from left/right, up/bottom to three
        while True:
            delete = []
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0:
                        continue
                    x0 = i
                    x1 = i
                    y0 = j
                    y1 = j
                    while x0 >= 0 and x0 > i - 3 and board[x0][j] == board[i][j]:
                        x0 -= 1
                    while x1 < m and x1 < i + 3 and board[x1][j] == board[i][j]:
                        x1 += 1
                    while y0 >= 0 and y0 > j - 3 and board[i][y0] == board[i][j]:
                        y0 -= 1
                    while y1 < n and y1 < j + 3 and board[i][y1] == board[i][j]:
                        y1 += 1
                    if x1 - x0 > 3 or y1 - y0 > 3:
                        delete.append([i,j])
            #board is stable
            if len(delete) == 0:
                break
            #make all candy crush to 0
            for candy in delete:
                board[candy[0]][candy[1]] = 0
            #move each 0 to the up and no crash's candies to bottom
            for j in range(n):
                t = m - 1
                for i in range(m-1,-1,-1):
                    if board[i][j] != 0:
                        board[t][j],board[i][j] = board[i][j],board[t][j]
                        t -= 1
        return board
