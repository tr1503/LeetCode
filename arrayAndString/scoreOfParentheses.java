class Solution {
    public int scoreOfParentheses(String S) {
        int res = 0;
        int left = 0;
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == '(')
                left++;
            else
                left--;
            if (S.charAt(i) == ')' && S.charAt(i - 1) == '(')
                res += 1 << left;
        }
        return res;
    }
}
