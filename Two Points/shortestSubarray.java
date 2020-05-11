class Solution {
    public int shortestSubarray(int[] A, int K) {
        int n = A.length;
        int res = n + 1;
        int[] s = new int[n + 1];
        for (int i = 0; i < n; i++) {
            s[i + 1] = s[i] + A[i];
        }
        Deque<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n + 1; i++) {
            while (!queue.isEmpty() && s[i] - s[queue.peekFirst()] >= K) {
                res = Math.min(res, i - queue.pollFirst());
            }
            while (!queue.isEmpty() && s[i] <= s[queue.peekLast()]) {
                queue.pollLast();
            }
            queue.offerLast(i);
        }
        return res == n + 1 ? -1 : res;
    }
}
