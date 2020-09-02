class Solution {
    public String encode(String s) {
        int n = s.length();
        if (s.length() <= 3)
            return s;
        
        String[][] dp = new String[n][n];
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i < n - len + 1; i++) {
                int j = i + len - 1;
                dp[i][j] = s.substring(i, i + len);
                
                if (len <= 3)
                    continue;
                for (int k = i; k < j; k++) {
                    String left = dp[i][k];
                    String right = dp[k + 1][j];
                    if (left.length() + right.length() < dp[i][j].length())
                        dp[i][j] = dp[i][k] + dp[k + 1][j];
                }
                String str = encode(dp, s.substring(i, i + len), i);
                if (str.length() < dp[i][j].length())
                    dp[i][j] = str;
            }
        }
        return dp[0][n - 1];
    }
    
    private String encode(String[][] dp, String s, int start) {
        int index = (s + s).indexOf(s, 1);
        if (index >= s.length())
            return s;
        else
            return (s.length() / index) + "[" + dp[start][start + index - 1] + "]";
    }
}
