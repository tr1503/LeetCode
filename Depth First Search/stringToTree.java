// Use post-order dfs to solve this problem
// time is O(n), space is O(1)
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
    private int i = 0;
    
    public TreeNode str2tree(String s) {
        if (s.equals(""))
            return null;
        return dfs(s);
    }
    
    private TreeNode dfs(String s) {
        TreeNode root = null;
        if (s.charAt(i) != '(') {
            root = new TreeNode(getIntVal(s));
        }
        
        TreeNode leftNode = null, rightNode = null;
        if (i < s.length() && s.charAt(i) == '(') {
            i++;
            leftNode = dfs(s);
        }
        if (i < s.length() && s.charAt(i) == '(') {
            i++;
            rightNode = dfs(s);
        }
        // if not ( it must be ) otherwise i == s.length()
        // then return the current stack
        root.left = leftNode;
        root.right = rightNode;
        i++;
        return root;
    }
    
    private int getIntVal(String s) {
        StringBuilder sb = new StringBuilder();
        while (i < s.length()) {
            if (s.charAt(i) == '(' || s.charAt(i) == ')')
                break;
            sb.append(s.charAt(i));
            i++;
        }
        int val = Integer.valueOf(sb.toString());
        return val;
    }
}
