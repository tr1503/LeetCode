// use dfs to search each element in the matrix for four directions, time is O(4n^2)
class Solution {
    public int longestLine(int[][] M) {
        if (M == null || M.length == 0 || M[0] == null || M[0].length == 0)
            return 0;
        int m = M.length;
        int n = M[0].length;
        int res = 0;
        int[][] dirs = new int[][]{{1,0},{0,1},{-1,-1},{-1,1}};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (M[i][j] == 0)
                    continue;
                for (int k = 0; k < 4; k++) {
                    int x = i;
                    int y = j;
                    int count = 0;
                    while (x >= 0 && y >= 0 && x < m && y < n && M[x][y] == 1) {
                        x += dirs[k][0];
                        y += dirs[k][1];
                        count++;
                    }
                    res = Math.max(res, count);
                }
            }
        }
        return res;
    }
}
