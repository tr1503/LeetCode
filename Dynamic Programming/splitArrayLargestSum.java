class Solution {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        int[] sums = new int[n];
        // dp[i][j] = min of largest sum of splitting nums[0] to nums[j] into i groups
        int[][] dp = new int[m+1][n];
        for (int[] row : dp) {
            Arrays.fill(row,Integer.MAX_VALUE);
        }
        sums[0] = nums[0];
        for (int i = 1; i < n; i++) {
            sums[i] += sums[i-1] + nums[i];
        }
        for (int i = 0; i < n; i++) {
            dp[1][i] = sums[i];
        }
        
        for (int i = 2; i <= m; i++) {
            for (int j = i - 1; j < n; j++) {
                for (int k = 0; k < j; k++) {
                    dp[i][j] = Math.min(dp[i][j],Math.max(dp[i-1][k], sums[j] - sums[k]));
                }
            }
        }
        return dp[m][n-1];
    }
}
