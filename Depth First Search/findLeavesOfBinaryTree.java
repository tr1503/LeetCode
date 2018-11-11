/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// Use dfs to get the depth of each tree node, add this tree node's value to 
// the array whose index is its depth.
class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> findLeaves(TreeNode root) {
        dfs(root);
        return res;
    }
    
    private int dfs(TreeNode root) {
        if (root == null)
            return -1;
        int depth = 1 + Math.max(dfs(root.left),dfs(root.right));
        if (depth + 1 > res.size()) {
            res.add(new ArrayList<Integer>());
        }
        res.get(depth).add(root.val);
        return depth;
    }
}
