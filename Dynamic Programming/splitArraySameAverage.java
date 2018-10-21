class Solution {
    public boolean splitArraySameAverage(int[] A) {
        int len = A.length;
        int[] sum = new int[len];
        sum[0] = A[0];
        int max = Integer.MAX_VALUE;
        for (int i = 1; i < sum.length; i++) {
            sum[i] = sum[i-1] + A[i];
        }
        float division = (float)sum[len - 1] / len;
        float[][][] dp = new float[2][len][sum[len - 1] + 1];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j <= i; j++) {
                for (int k = 0; k <= sum[i]; k++) {
                    dp[i%2][j][k] = max;
                    dp[i%2][0][A[i]] = 1;
                    if ((k >= A[i] && i > 0 && j > 0 && dp[(i-1) % 2][j - 1][k - A[i]] != max) || (i > 0 && j <= i - 1 && k <= sum[i-1] && dp[(i-1) % 2][j][k] != max)) {
                        dp[i%2][j][k] = (float) k / (j + 1);
                    }
                    if (i == len - 1 && j > 0 && j < len - 1 && dp[i%2][j][k] == division)
                        return true;
                }
            }
        }
        return false;
    }
}
