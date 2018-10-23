// Use dynamic programming to solve this question
// The each element in dp reprents the how many ways for coin change
// Time is O(amount * len(coins)), space is O(amount)
// Check https://www.youtube.com/watch?v=ZKAILBWl08g
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp,0);
        dp[0] = 1;
        
        for (int i = 1; i <= coins.length; i++) {
            for (int j = 0; j <= amount; j++) {
                if (coins[i - 1] <= j) {
                    dp[j] += dp[j - coins[i - 1]];
                }
            }
        }
        return dp[amount];
    }
}
