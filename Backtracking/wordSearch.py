class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dfs(board,i,j,word,0))
                    return true;
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, int i, int j, String word, int start) {
        if (start >= word.length())
            return true;
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length)
            return false;
        if (board[i][j] == word.charAt(start++)) {
            char c = board[i][j];
            board[i][j] = '#';
            boolean res = dfs(board,i+1,j,word,start) || dfs(board,i-1,j,word,start) ||
                dfs(board,i,j-1,word,start) || dfs(board,i,j+1,word,start);
            board[i][j] = c;
            return res;
        }
        return false;
    }
}
