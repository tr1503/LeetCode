// use hash map and two init values min and max to order the level-order's result in vertical order
// time is O(n), space is O(n)
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
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null)
            return res;
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        Queue<TreeNode> queue = new LinkedList<>();
        Queue<Integer> cols = new LinkedList<>();
        
        queue.add(root);
        cols.add(0);
        
        int min = 0;
        int max = 0;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            int col = cols.poll();
            if (!map.containsKey(col)) 
                map.put(col, new ArrayList<Integer>());
            map.get(col).add(node.val);
            
            if (node.left != null) {
                queue.add(node.left);
                cols.add(col - 1);
                if (col <= min) 
                    min = col - 1;
            }
            
            if (node.right != null) {
                queue.add(node.right);
                cols.add(col + 1);
                if (col >= max) 
                    max = col + 1;
            }
        }
        
        for (int i = min; i <= max; i++) {
            res.add(map.get(i));
        }
        
        return res;
    }
}
