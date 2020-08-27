/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int res;
    
    public int maxAncestorDiff(TreeNode root) {
        if (root == null)
            return 0;
        res = 0;
        dfs(root, root.val, root.val);
        return res;
    }
    
    private void dfs(TreeNode root, int min, int max) {
        if (root == null)
            return;
        int diff1 = Math.abs(root.val - min);
        int diff2 = Math.abs(root.val - max);
        res = Math.max(res, diff1);
        res = Math.max(res, diff2);
        dfs(root.left, Math.min(min, root.val), Math.max(max, root.val));
        dfs(root.right, Math.min(min, root.val), Math.max(max, root.val));
    }
}
