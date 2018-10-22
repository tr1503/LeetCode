//Use blanced tree table in java, time is O(nlogn)
class Solution {
    public int kEmptySlots(int[] flowers, int k) {
        TreeSet<Integer> set = new TreeSet<>();
        int i = 0;
        for (int n : flowers) {
            set.add(n);
            int prev = n - k - 1;
            int next = n + k + 1;
            if (set.contains(prev)) {
                Integer p = set.ceiling(prev + 1);
                if (p != null && p == n)
                    return set.size();
            }
            if (set.contains(next)) {
                Integer t = set.floor(next - 1);
                if (t != null && t == n)
                    return set.size();
            }
        }
        return -1;
    }
}
