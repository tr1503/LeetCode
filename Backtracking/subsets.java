class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> arr = new ArrayList<Integer>();
        dfs(res,arr,nums,0,0);
        return res;
    }
    private void dfs(List<List<Integer>> res, List<Integer> arr, int[] nums, int pos, int iter) {
        res.add(new ArrayList<Integer>(arr));
        if (pos == nums.length) {
            return;
        }
        //Only choose the numbers after this iter index, prevent repeating
        for (int i = iter; i < nums.length; i++) {
            if (arr.contains(nums[i]))
                continue;
            arr.add(nums[i]);
            dfs(res,arr,nums,pos+1,i);
            arr.remove(arr.size() - 1);
        }
    }
}
