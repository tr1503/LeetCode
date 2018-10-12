/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//Use serialize binary tree and hashtable to set each subtree as a key in hashtable
//If the value of key = 2, add this tree node to result. Time is O(n^2), space is O(n^2).
class Solution {
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        HashMap<String,Integer> map = new HashMap<>();
        List<TreeNode> list = new ArrayList<>();
        serialize(root,map,list);
        return list;
    }
    
    private String serialize(TreeNode root, HashMap<String,Integer> map, List<TreeNode> list) {
        if (root == null)
            return "#";
        String key = Integer.toString(root.val) + "," + serialize(root.left,map,list) + "," + serialize(root.right,map,list);
        if (!map.containsKey(key))
            map.put(key,1);
        else
            map.put(key,map.get(key) + 1);
        if (map.get(key) == 2)
            list.add(root);
        return key;
    }
}
