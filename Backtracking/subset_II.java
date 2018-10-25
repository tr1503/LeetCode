// Use backtracking to do this question, time is O(2^n), space is O(n).
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0)
            return res;
        Arrays.sort(nums);
        dfs(res,new ArrayList<>(), nums, 0);
        return res;
    }
    
    private void dfs(List<List<Integer>> res, List<Integer> list, int[] nums, int pos) {
        res.add(new ArrayList<>(list));
        for (int i = pos; i < nums.length; i++) {
            // remember to delete the duplicates when this number is a duplicate in array
            if (i != pos && nums[i] == nums[i-1])
                continue;
            list.add(nums[i]);
            dfs(res,list,nums,i+1);
            list.remove(list.size() - 1);
        }
    }
}
