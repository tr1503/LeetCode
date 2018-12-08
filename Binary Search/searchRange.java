// Use two binary search to find the result
class Solution {
    public int[] searchRange(int[] nums, int target) {
        // set the init value to -1, -1
        int[] res = {-1, -1};
        if (nums == null || nums.length == 0)
            return res;
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < target) 
                lo = mid + 1;
            else
                hi = mid;
        }
        if (nums[lo] != target) {
            return res;
        }
        else {
            res[0] = lo;
        }
        hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2 + 1;
            if (nums[mid] > target)
                hi = mid - 1;
            else
                lo = mid;
        }
        res[1] = hi;
        return res;
    }
}
