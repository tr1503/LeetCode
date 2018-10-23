// Use a dp array to store the value calculated
// Check https://leetcode.com/problems/target-sum/discuss/97334/Java-(15-ms)-C%2B%2B-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanation
class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        // >>> 1 is equal to / 2 to prevent overflow for large number
        return sum < S || (S + sum) % 2 > 0 ? 0 : subsetSum(nums, (S + sum) >>> 1);
    }
    
    private int subsetSum(int[] nums, int S) {
        int[] dp = new int[S+1];
        dp[0] = 1;
        for (int n : nums) {
            for (int i = S; i >= n; i--) {
                dp[i] += dp[i - n];
            }
        }
        return dp[S];
    }
}
