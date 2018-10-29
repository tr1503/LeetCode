class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        if (nums == null || nums.length == 0)
            return res;
        int start = nums[0];
        int end = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] + 1 != nums[i]) {
                res.add(getRange(start,end));
                start = nums[i];
            }
            end = nums[i];
        }
        res.add(getRange(start,end));
        return res;
    }
    
    private String getRange(int start, int end) {
        StringBuilder sb = new StringBuilder();
        if (start == end) {
            sb.append(start);
        }
        else if (start < end) {
            sb.append(start);
            sb.append("->");
            sb.append(end);
        }
        return sb.toString();
    }
}
