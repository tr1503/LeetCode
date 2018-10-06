class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<List<Integer>>(); 
        if (k > n || k < 0) {
            return res;
        }
        if (k == 0) {
            res.add(new ArrayList<Integer>());
            return res;
        }
        res = combine(n-1,k-1);
        for (List<Integer> list: res) {
            list.add(n);
        }
        res.addAll(combine(n-1,k));
        return res;
    }
}
