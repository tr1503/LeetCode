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
    private int max = 1;
    public int longestConsecutive(TreeNode root) {
        if (root == null)
            return 0;
        helper(root);
        return max;
    }
    
    private int[] helper(TreeNode root) {
        if (root == null)
            return null;
        int[] right = helper(root.right);
        int[] left = helper(root.left);
        int[] res = new int[] {1,1};
        if (right == null && left == null)
            return res;
        
        if (root.right != null) {
            if (root.val == root.right.val + 1) {
                max = Math.max(max, right[0] + 1);
                res[0] = right[0] + 1;
                res[1] = 1;
            }
            else if (root.val == root.right.val - 1) {
                max = Math.max(max, right[1] + 1);
                res[0] = 1;
                res[1] = right[1] + 1;
            } 
        }
        
        if (root.left != null) {
            if (root.val == root.left.val + 1) {
                max = Math.max(max, left[0] + res[1]);
                res[0] = Math.max(res[0], left[0] + 1);
            }
            else if (root.val == root.left.val - 1) {
                max = Math.max(max, left[1] + res[0]);
                res[1] = Math.max(res[1], left[1] + 1);
            } 
        }
        return res;
    }
}
