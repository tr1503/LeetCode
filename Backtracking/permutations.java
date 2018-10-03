class Solution {
    private List<List<Integer>> res = new ArrayList<List<Integer>>();
    private int length;
    
    public List<List<Integer>> permute(int[] nums) {
        length = nums.length;
        List <Integer> select = new ArrayList<Integer>();
        helper(select,nums,0);
        return res;
    }
    
    //s reprents the numbers which are used. nums reprents all numbers from pool. pos represents the position of value we should pick.
    private void helper(List<Integer>s, int[] nums, int pos) {
        //All values from pool are picked, end recursion.
        if (pos == length) {
            res.add(new ArrayList<Integer>(s));
            return;
        }
        for (int i=0;i<nums.length;i++) {
            int num = nums[i];
            //Skip repeated value
            if(s.contains(num)) 
                continue;
            s.add(num);
            helper(s,nums,pos+1);
            //Important: remove the last value to backtrack.
            s.remove(s.size() - 1);
        }
    }
}
