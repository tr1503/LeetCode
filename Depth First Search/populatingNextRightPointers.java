/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
            connect(root,null);
        }
        private static void connect(TreeLinkNode root, TreeLinkNode sibling) {
            if (root == null)
                return;
            else root.next = sibling;
            connect(root.left,root.right);
            if (sibling != null)
                connect(root.right, sibling.left);
            else
                connect(root.right, null);
        }
}
