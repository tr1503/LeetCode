//Use two points to solve this question, the time is O(n).
//See http://www.cnblogs.com/grandyang/p/8684817.html
class Solution {
    public String minWindow(String S, String T) {
        if (S.length() == 0 || T.length() == 0)
            return "";
        int s = S.length();
        int t = T.length();
        int start = -1;
        int min = Integer.MAX_VALUE;
        int i = 0;
        int j = 0;
        while (i < s) {
            if (S.charAt(i) == T.charAt(j)) {
                if (++j == t) {
                    int end = i + 1;
                    while (--j >= 0) {
                        while (S.charAt(i--) != T.charAt(j));
                    }
                    i++;
                    j++;
                    if (end - i < min) {
                        min = end - i;
                        start = i;
                    }
                }
            }
            i++;
        }
        return (start != -1) ? S.substring(start,start + min) : "";
    }
}
