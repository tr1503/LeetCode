class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> ranges = new HashMap<>();
        int max = 0;
        for (int num : nums) {
            if (ranges.containsKey(num))
                continue;
            // find left and right num
            int left = ranges.getOrDefault(num - 1, 0);
            int right = ranges.getOrDefault(num + 1, 0);
            int sum = left + right + 1;
            max = Math.max(max, sum);
            
            // union by updating boundary
            // leave middle k-v dirty to avoid cascading update
            if (left > 0)
                ranges.put(num - left, sum);
            if (right > 0)
                ranges.put(num + right, sum);
            ranges.put(num, sum);
        }
        return max;
    }
}
