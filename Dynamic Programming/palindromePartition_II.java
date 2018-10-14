class Solution {
    public int minCut(String s) {
        int n = s.length();
        boolean[][] matrix = new boolean[n][n];
        int[] cuts = new int[n+1];
        if (s == null || s.length() == 0)
            return 0;
        for (int i = 0; i < n; i++) {
            cuts[i] = n - i;
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if ((s.charAt(i) == s.charAt(j) && j - i < 2) || (s.charAt(i) == s.charAt(j) && matrix[i+1][j-1])) {
                    matrix[i][j] = true;
                    cuts[i] = Math.min(cuts[i],cuts[j+1] + 1);
                }
            }
        }
        return cuts[0] - 1;
    }
}
