class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums == null || nums.length == 0 || k <= 0 || t < 0) {
            return false;
        }
        //Use Java's tree set(self-balanced tree) to store the value
        TreeSet<Integer> tree = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            Integer ceil = tree.ceiling(nums[i]);
            if (ceil != null && Long.valueOf(ceil) - Long.valueOf(nums[i]) <= t) 
                return true;
            Integer floor = tree.floor(nums[i]);
            if (floor != null && Long.valueOf(nums[i]) - Long.valueOf(floor) <= t)
                return true;
            tree.add(nums[i]);
            //Sliding window, delete useless previous value from tree
            if (i >= k) {
                tree.remove(nums[i-k]);
            }
        }
        return false;
    }
}
