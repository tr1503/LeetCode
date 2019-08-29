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
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null)
                break;
            queue.offer(node.left);
            queue.offer(node.right);
        }
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null)
                return false;
        }
        return true;
    }
}
