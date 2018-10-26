// use dp to memeorize the calculated numbers 
// check https://github.com/awangdev/LeetCode/blob/master/Java/Burst%20Balloons.java
class Solution {
    int[][] dp;
    int[] values;
    public int maxCoins(int[] nums) {
        if (nums == null || nums.length == 0)
            return 0;
        int n = nums.length;
        dp = new int[n + 2][n + 2];
        values = new int[n+2];
        values[0] = values[n+1] = 1;
        for (int i = 1; i < n + 1; i++) {
            values[i] = nums[i-1];
        }
        return DP(1,n);
    }
    
    private int DP(int i, int j) {
        if (dp[i][j] > 0) {
            return dp[i][j];
        }
        for (int x = i; x <= j; x++) {
            dp[i][j] = Math.max(dp[i][j], DP(i, x - 1) + values[i-1] * values[x] * values[j+1] + DP(x+1,j));
        }
        return dp[i][j];
    }
}
