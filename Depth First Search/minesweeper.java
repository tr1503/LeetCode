// Use dfs (recursion) to update the neighbor's value
// See http://www.cnblogs.com/grandyang/p/6536694.html the second way
class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        if (board == null || board.length == 0 || board[0] == null || board[0].length == 0) 
            return new char[][] {};
        int m = board.length;
        int n = board[0].length;
        int x = click[0];
        int y = click[1];
        int count = 0;
        if (board[x][y] == 'M') {
            board[x][y] = 'X';
        }
        else {
            List<int[]> neighbors = new ArrayList<>();
            for (int i = -1; i < 2; i++) {
                for (int j = -1; j < 2; j++) {
                    int nx = x + i;
                    int ny = y + j;
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                        continue;
                    if (board[nx][ny] == 'M')
                        count++;
                    else if (count == 0 && board[nx][ny] == 'E')
                        neighbors.add(new int[]{nx,ny});
                }
            }
            if (count > 0)
                board[x][y] = (char)(count + '0');
            else {
                for (int[] a : neighbors) {
                    board[a[0]][a[1]] = 'B';
                    updateBoard(board,a);
                }
            }
        }
        return board;
    }
}
