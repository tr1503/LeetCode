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
    private int ans;
    public int longestUnivaluePath(TreeNode root) {
        if (root == null)
            return 0;
        this.ans = 0;
        univaluePath(root);
        return this.ans;
    }
    
    private int univaluePath(TreeNode root) {
        if (root == null)
            return 0;
        int left = univaluePath(root.left);
        int right = univaluePath(root.right);
        int pl = 0;
        int pr = 0;
        if (root.left != null && root.val == root.left.val)
            pl = left + 1;
        if (root.right != null && root.val == root.right.val)
            pr = right + 1;
        this.ans = Math.max(this.ans, pl + pr);
        return Math.max(pl,pr);
    }
}
