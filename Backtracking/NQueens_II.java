class Solution {
    int res = 0;
    public int totalNQueens(int n) {
        if (n <= 0)
            return 0;
        helper(new int[n],0);
        return res;
    }
    
    private void helper(int[] queens, int pos) {
        if (pos == queens.length) {
            res++;
            return;
        }
        for (int i = 0; i < queens.length; i++) {
            queens[pos] = i;
            if (isValid(queens, pos)) {
                helper(queens, pos + 1);
            }
        }
    }
    
    private boolean isValid(int[] queens, int pos) {
        for (int i = 0; i < pos; i++) {
            if (queens[i] == queens[pos] || Math.abs(queens[pos] - queens[i]) == Math.abs(i - pos)) { 
                // check if they are same column and same diagonal line
                return false;
            }
        }
        return true;
    }
}
