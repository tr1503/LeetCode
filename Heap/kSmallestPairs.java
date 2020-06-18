class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        k = Math.min(k, nums1.length * nums2.length);
        List<List<Integer>> res = new ArrayList<>(k);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] + a[1]) - (b[0] + b[1]));
        int left = 0;
        int right = 0;
        for (int i = 0; i < Math.min(k, nums1.length); i++) {
            pq.offer(new int[]{nums1[i], nums2[0], 0});
        }
        for (int i = 0; i < k; i++) {
            int[] arr = pq.poll();
            List<Integer> pair = new ArrayList<>();
            pair.add(arr[0]);
            pair.add(arr[1]);
            res.add(pair);
            if (nums2.length > arr[2] + 1)
                pq.offer(new int[]{arr[0], nums2[++arr[2]], arr[2]});
        }
        return res;
    }
}
