// Use 1 represents player 1's move and -1 represents player 2's move
// if cols, rows and diagonals' absolate value is equal to n, return the winner
// move() time is O(1)
class TicTacToe {
    private int[] rows;
    private int[] cols;
    private int diagonal1;
    private int diagonal2;
    
    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        rows = new int[n];
        cols = new int[n];
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        int n = rows.length;
        int move = player == 1 ? 1 : -1;
        rows[row] += move;
        cols[col] += move;
        if (row == col) {
            diagonal1 += move;
        }
        if (row + col == n - 1) {
            diagonal2 += move;
        }
        
        if (Math.abs(rows[row]) == n || Math.abs(cols[col]) == n 
            || Math.abs(diagonal1) == n || Math.abs(diagonal2) == n) {
            return player;
        }
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
