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
    public int maxPathSum(TreeNode root) {
        if (root == null)
            return 0;
        int[] maxPath = new int[]{Integer.MIN_VALUE};
        dfs(root,maxPath);
        return maxPath[0];
    }
    
    //Use dfs to get the max path from the root to up and bottom directly
    private int dfs(TreeNode root, int[] maxPath) {
        int left = root.left != null ? Math.max(dfs(root.left,maxPath),0) : 0;
        int right = root.right != null ? Math.max(dfs(root.right,maxPath),0) : 0;
        int curr = root.val + left + right;
        maxPath[0] = Math.max(maxPath[0],curr);
        return root.val + Math.max(left,right);
    }
}
