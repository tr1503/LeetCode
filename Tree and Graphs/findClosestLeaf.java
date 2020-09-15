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
    public int findClosestLeaf(TreeNode root, int k) {
        Map<TreeNode, TreeNode> map = new HashMap<>();
        Queue<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();
        
        TreeNode target = dfs(root, k, map);
        queue.add(target);
        visited.add(target);
        
        while (!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            if (curr.left == null && curr.right == null)
                return curr.val;
            if (curr.left != null && !visited.contains(curr.left)) {
                queue.add(curr.left);
                visited.add(curr.left);
            }
            if (curr.right != null && !visited.contains(curr.right)) {
                queue.add(curr.right);
                visited.add(curr.right);
            }
            if (map.containsKey(curr) && !visited.contains(map.get(curr))) {
                queue.add(map.get(curr));
                visited.add(map.get(curr));
            }
        }
        return -1;
    }
    
    private TreeNode dfs(TreeNode root, int k, Map<TreeNode, TreeNode> map) {
        if (root.val == k)
            return root;
        if (root.left != null) {
            map.put(root.left, root);
            TreeNode left = dfs(root.left, k, map);
            if (left != null)
                return left;
        }
        if (root.right != null) {
            map.put(root.right, root);
            TreeNode right = dfs(root.right, k, map);
            if (right != null)
                return right;
        }
        return null;
    }
}
