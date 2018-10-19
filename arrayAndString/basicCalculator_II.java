class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0)
            return 0;
        s = s.trim().replaceAll(" +","");
        int res = 0;
        int prev = 0;
        int i = 0;
        int sign = '+';
        while (i < s.length()) {
            int curr = 0;
            while (i < s.length() && Character.isDigit(s.charAt(i))) {
                curr = curr * 10 + s.charAt(i) - '0';
                i++;
            }
            if (sign == '+') {
                res += prev;
                prev = curr;
            }
            else if (sign == '-') {
                res += prev;
                prev = -curr;
            }
            else if (sign == '*') {
                prev = prev * curr;
            }
            else if (sign == '/') {
                prev = prev / curr;
            }
            if (i < s.length()) {
                sign = s.charAt(i);
                i++;
            }
        }
        res += prev;
        return res;
    }
}
