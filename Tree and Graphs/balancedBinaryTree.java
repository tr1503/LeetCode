/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private boolean res = true;
    public boolean isBalanced(TreeNode root) {
        maxDepth(root);
        return res;
    }
    private int maxDepth(TreeNode root) {
        if (root == null) 
            return 0;
        int l = maxDepth(root.left);
        int r = maxDepth(root.right);
        if (Math.abs(l-r) > 1)
            res = false;
        return 1 + Math.max(l,r);
    }
}
