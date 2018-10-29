/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val,Node _next) {
        val = _val;
        next = _next;
    }
};
*/
class Solution {
    public Node insert(Node head, int insertVal) {
        if (head == null) {
            Node newNode = new Node(insertVal);
            newNode.next = newNode;
            return newNode;
        } 
        Node node = head;
        while (node != null && node.next != null) {
            if (node.val < node.next.val) {
                if (node.val <= insertVal && node.next.val >= insertVal) {
                    insertNode(node,insertVal);
                    break;
                }
            }
            else if (node.val > node.next.val) {
                if (insertVal > node.val || insertVal < node.next.val) {
                    insertNode(node,insertVal);
                    break;
                }
            }
            else { // node.val == node.next.val
                if (node.next == head) {
                    insertNode(node,insertVal);
                    break;
                }
            }
            node = node.next;
        }
        return head;
    }
    
    private void insertNode(Node node, int val) {
        Node newNode = new Node(val);
        newNode.next = node.next;
        node.next = newNode;
    }
}
