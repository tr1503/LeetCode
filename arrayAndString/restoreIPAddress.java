// brute-force search all possible combination because ip address only has three numbers for each part
// time is n / 3, space is constant
class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<>();
        int len = s.length();
        StringBuffer ip = new StringBuffer();
        for (int a = 1; a <= 3; a++) {
            for (int b = 1; b <= 3; b++) {
                for (int c = 1; c <= 3; c++) {
                    int d = len - a - b - c;
                    if (d > 0 && d <= 3 && a + b + c + d == len) {
                        int A = Integer.parseInt(s.substring(0, a));
                        int B = Integer.parseInt(s.substring(a, a + b));
                        int C = Integer.parseInt(s.substring(a + b, a + b + c));
                        int D = Integer.parseInt(s.substring(a + b + c));
                        if (A <= 255 && B <= 255 && C <= 255 && D <= 255) {
                            ip.append(A).append(".").append(B).append(".").append(C).append(".").append(D);
                            if (ip.length() == len + 3) {
                                res.add(ip.toString());
                            }
                            ip = new StringBuffer();
                        }
                    }
                }
            }
        }
        return res;
    }
}
