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
    public boolean isValidSequence(TreeNode root, int[] arr) {
        return helper(root, arr, 0);
    }
    
    private boolean helper(TreeNode root, int[] arr, int index) {
        if (root.left == null && root.right == null && index == arr.length - 1)
            return root.val == arr[index];
        if (root.left == null && root.right == null || index == arr.length - 1)
            return false;
        if (root.val != arr[index])
            return false;
        if (root.left != null && helper(root.left, arr, index + 1))
            return true;
        if (root.right != null && helper(root.right, arr, index + 1))
            return true;
        return false;
    }
}
