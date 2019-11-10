class Solution {
    public int gcd(int a, int b) {
        if (b > 0) {
            return gcd(b, a % b);
        }
        return a;
    }
    
    public boolean hasGroupsSizeX(int[] deck) {
        Map<Integer, Integer> count = new HashMap<>();
        int res = 0;
        for (int i : deck) {
            count.put(i, count.getOrDefault(i, 0) + 1);
        }
        for (int i : count.values()) {
            res = gcd(i, res);
        }
        return res > 1;
    }
}
