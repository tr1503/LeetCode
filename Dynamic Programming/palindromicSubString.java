/*
Use the same way from Longest Palindromic Substring. 
Create a recursion function from around center to left and right.
It needs [i,i] and [i,i+1] for even length's and odd length's palindroms.
Add all results to get answer.
*/
class Solution {
    public int countSubstrings(String s) {
        if (s == null || s.length() < 1) return 0;
        int start = 0;
        int end = 0;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            int res1 = expandAroundCenter(s,i,i);
            int res2 = expandAroundCenter(s,i,i+1);
            res += res1 + res2;
        }
        return res;
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left --;
            right ++;
            count ++;
        }
        return count;
    }
}
