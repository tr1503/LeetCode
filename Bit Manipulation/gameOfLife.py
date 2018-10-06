class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m > 0:
            n = len(board[0])
        else:
            n = 0
        for i in range(m):
            for j in range(n):
                lives = 0
                #Scan the 3x3 region including (i,j)
                for y in range(max(0, i-1), min(m,i+2)):
                    for x in range(max(0, j-1), min(n,j+2)):
                        lives += board[y][x] & 1
                #The numbers of lives is 3 or the numbers of lives - the live state is 3, this cell will be live
                if lives == 3 or lives - board[i][j] == 3:
                    #Make this cell live, 0b10 is 1, 1 or any number is 1
                    board[i][j] |= 0b10
        #Update each cell to next state
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
