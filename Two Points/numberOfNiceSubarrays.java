class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int n = nums.length;
        int res = 0, count = 0, temp = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (nums[i] % 2 == 1) {
                count++;
                if (count == k)
                    temp = 0;
                while (count == k) {
                    temp++;
                    if (nums[j] % 2 == 1)
                        count--;
                    j++;
                }
            }
            res += temp;
        }
        return res;
    }
}
