/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
// Use dfs and hash map to solve this question
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null)
            return null;
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
        UndirectedGraphNode head = new UndirectedGraphNode(node.label);
        map.put(node, head);
        dfs(map, node);
        return head;
    }
    
    private void dfs(HashMap<UndirectedGraphNode, UndirectedGraphNode> map, UndirectedGraphNode node) {
        if (node == null)
            return;
        for (UndirectedGraphNode neighbor : node.neighbors) {
            if (!map.containsKey(neighbor)) { // map doesn't have the neighbors, need to be added
                UndirectedGraphNode newNode = new UndirectedGraphNode(neighbor.label);
                map.put(neighbor, newNode);
                dfs(map,neighbor);
            }
            map.get(node).neighbors.add(map.get(neighbor));
        }
    }
}
