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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTree(preorder,0,preorder.length,inorder,0,inorder.length);
    }
    
    TreeNode buildTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
        if (preStart == preEnd)
            return null;
        if (inStart == inEnd)
            return null;
        
        TreeNode root = new TreeNode(preorder[preStart]);
        int index = find(inorder,inStart,inEnd,preorder[preStart]);
        int leftSize = index - inStart;
        
        root.left = buildTree(preorder, preStart + 1, preStart + leftSize + 1, inorder, inStart, inStart + leftSize);
        root.right = buildTree(preorder, preStart + leftSize + 1, preEnd, inorder, index + 1, inEnd);
        return root;
    }
    
    private int find(int[] order, int start, int end, int val) {
        for (int i = start; i < end; i++) {
            if (order[i] == val)
                return i;
        }
        return -1;
    }
}
