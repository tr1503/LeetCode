class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        dfs(res, new ArrayList<Integer>(), target, candidates, 0);
        return res;
    }
    
    private void dfs(List<List<Integer>> res, List<Integer> path, int target, int[] candidates, int index) {
        if (target == 0)
            res.add(new ArrayList<>(path));
        for (int j = index; j < candidates.length && target >= candidates[j]; j++) {
            // Prevent the duplicated results
            if (j > index && candidates[j] == candidates[j-1])
                continue;
            path.add(candidates[j]);
            dfs(res, path, target - candidates[j], candidates, j + 1);
            path.remove(path.size() - 1);
        }
    }
}
