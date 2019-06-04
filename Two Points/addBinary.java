// Use two pointers from the end of two strings
// If one string is iterated, put 0
// The result should be the mod of sum / 2, the carry should be the result of sum / 2
// If carry is still 1, put it at the beginning of the result
class Solution {
    public String addBinary(String a, String b) {
        String res = "";
        int m = a.length() - 1;
        int n = b.length() - 1;
        int carry = 0;
        while (m >= 0 || n >= 0) {
            int p = m >= 0 ? a.charAt(m) - '0' : 0;
            int q = n >= 0 ? b.charAt(n) - '0' : 0;
            m--;
            n--;
            int sum = p + q + carry;
            res = Integer.toString(sum % 2) + res;
            carry = sum / 2;
        }
        return carry == 1 ? "1" + res : res;
    }
}
