// Build a graph instead of tree and bfs this graph with queue and hash set
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
    Map<Integer, List<Integer>> graph = new HashMap<>();
    
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        buildGraph(null, root);
        List<Integer> res = new LinkedList<>();
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        int distance = 0;
        queue.offer(target.val);
        visited.add(target.val);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int curr = queue.poll();
                if (distance == K) {
                    res.add(curr);
                }
                if (graph.containsKey(curr)) {
                    for (int neigh : graph.get(curr)) {
                        if (visited.contains(neigh))
                            continue;
                        queue.offer(neigh);
                        visited.add(neigh);
                    }
                }
            }
            distance++;
        }
        return res;
    }
    
    private void buildGraph(TreeNode parent, TreeNode child) {
        if (parent != null) {
            graph.computeIfAbsent(parent.val, x -> new LinkedList<>()).add(child.val);
            graph.computeIfAbsent(child.val, x -> new LinkedList<>()).add(parent.val);
        }
        if (child.left != null) {
            buildGraph(child, child.left);
        }
        if (child.right != null) {
            buildGraph(child, child.right);
        }
    }
}
