class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        dfs(new LinkedList<Integer>(), 0, nums, res);
        return res;
    }
    
    private void dfs(LinkedList<Integer> list, int index, int[] nums, List<List<Integer>> res) {
        if (list.size() > 1) {
            res.add(new LinkedList<Integer>(list));
        }
        // Use set to store used number to prevent repeating use
        Set<Integer> used = new HashSet<>();
        for (int i = index; i < nums.length; i++) {
            if (used.contains(nums[i]))
                continue;
            // If we can create a new subsequence or we can add this num to existing subsequence
            if (list.size() == 0 || nums[i] >= list.peekLast()) {
                used.add(nums[i]);
                list.add(nums[i]);
                dfs(list,i+1,nums,res);
                list.remove(list.size() - 1);
            }
        }
    }
}
