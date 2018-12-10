// Use binary search and two pointers to solve this problem like 3Sum. The time is O(n^2logn)
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            for (int j = i + 1; j < nums.length - 2; j++) {
                int left = j + 1;
                int right = nums.length - 1;
                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        List<Integer> tuple = new ArrayList<>();
                        tuple.add(nums[i]);
                        tuple.add(nums[j]);
                        tuple.add(nums[left]);
                        tuple.add(nums[right]);
                        if (!res.contains(tuple))
                            res.add(tuple);
                        left++;
                        right--;
                    }
                    else if (sum < target)
                        left++;
                    else 
                        right--;
                }
            }
        }
        return res;
    }
}
