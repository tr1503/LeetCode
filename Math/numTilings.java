class Solution {
    public int numTilings(int N) {
        int a = 0;
        int b = 1;
        int c = 1;
        int c2;
        int mod = 1000000007;
        while (--N > 0) {
            c2 = (c * 2 % mod + a) % mod;
            a = b;
            b = c;
            c = c2;
        }
        return c;
    }
}
