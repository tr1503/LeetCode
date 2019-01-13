class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(k, n, 1, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(int k, int n, int index, List<Integer> path, List<List<Integer>> res) {
        if (n < 0)
            return;
        if (n == 0 && path.size() == k)
            res.add(new ArrayList<>(path));
        for (int i = index; i <= 9; i++) {
            path.add(i);
            dfs(k, n - i, i + 1, path, res);
            path.remove(path.size() - 1);
        }
    }
}
