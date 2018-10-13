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
        if (root == null)
            return;
        Queue<TreeLinkNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<TreeLinkNode> list = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeLinkNode curr = queue.poll();
                if (curr.left != null)
                    queue.offer(curr.left);
                if (curr.right != null)
                    queue.offer(curr.right);
                list.add(curr);
            }
            for (int i = 0; i < list.size() - 1; i++) {
                list.get(i).next = list.get(i+1);
            }
        }
    }
}
