class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        int maxLen = 0;
        for (String word : wordDict) {
            maxLen = Math.max(maxLen, word.length());
        }
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = Math.max(0, i - maxLen); j < i; j++) {
                if (dp[j] && set.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        if (!dp[n]) {
            return new ArrayList<String>();
        }
        List<String>[] memo = new List[n + 1];
        memo[0] = new ArrayList<>();
        memo[0].add("");
        for (int i = 1; i <= n; i++) {
            memo[i] = new ArrayList<>();
            for (int j = Math.max(0, i - maxLen); j < i; j++) {
                if (memo[j].size() > 0 && set.contains(s.substring(j, i))) {
                    String word = s.substring(j, i);
                    for (String sub : memo[j]) {
                        if (sub.equals(""))
                            memo[i].add(word);
                        else
                            memo[i].add(sub + " " + word);
                    }
                }
            }
        }
        return memo[n];
    }
}
