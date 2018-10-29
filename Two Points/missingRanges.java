// set a variable upperBelow as each element - 1 to compare with the lower bound of range
class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> res = new ArrayList<>();
        long low = (long)lower;
        long high = (long)upper;
        for (int num : nums) {
            long upperBelow = (long)num - 1;
            if (low == upperBelow) {
                res.add((int)low + "");
            }
            else if (low < upperBelow) {
                res.add((int)low + "->" + (int)upperBelow);
            }
            low = (long)num + 1;
        }
        if (low == high) {
            res.add((int)low + "");
        }
        else if (low < high) {
            res.add((int)low + "->" + (int)high);
        }
        return res;
    }
}
