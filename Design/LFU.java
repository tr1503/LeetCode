// use doubly linked list and hashmap to solve this question
// see https://www.jianshu.com/p/437f53341f67
class LFUCache {

    private static class Node {
        int key;
        int value;
        int freq = 0;
        Node next;
        Node prev;
        NodeQueue nq;
        
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private static class NodeQueue {
        NodeQueue next;
        NodeQueue prev;
        Node tail;
        Node head;
        
        public NodeQueue(NodeQueue next, NodeQueue prev, Node tail, Node head) {
            this.next = next;
            this.prev = prev;
            this.tail = tail;
            this.head = head;
        }
    }
    
    
    NodeQueue tail;
    int capacity;
    HashMap<Integer, Node> map;
        
    LFUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<Integer, Node>(capacity);
    }
    
    private void oneStepUp(Node n) {
        n.freq++;
        boolean singleQueue = false;
        if (n.nq.head == n.nq.tail)
            singleQueue = true;
        if (n.nq.next != null) {
            if (n.nq.next.tail.freq == n.freq) {
                removeNode(n);
                n.prev = n.nq.next.head;
                n.nq.next.head.next = n;
                n.nq.next.head = n;
                n.nq = n.nq.next;
            }
            else if (n.nq.next.tail.freq > n.freq) {
                if (!singleQueue) {
                    removeNode(n);
                    NodeQueue nnq = new NodeQueue(n.nq.next,n.nq,n,n);
                    n.nq.next.prev = nnq;
                    n.nq.next = nnq;
                    n.nq = nnq;
                }
            }        
        } else {
            if (!singleQueue) {
                removeNode(n);
                NodeQueue nnq = new NodeQueue(null,n.nq,n,n);
                n.nq.next = nnq;
                n.nq = nnq;
            }
        }
    }
    
    private Node removeNode(Node n) {
        if (n.nq.head == n.nq.tail) {
            removeNQ(n.nq);
            return n;
        }
        if (n.prev != null)
            n.prev.next = n.next;
        if (n.next != null)
            n.next.prev = n.prev;
        if (n.nq.head == n)
            n.nq.head = n.prev;
        if (n.nq.tail == n)
            n.nq.tail = n.next;
        n.prev = null;
        n.next = null;
        return n;
    }
    
    private void removeNQ(NodeQueue nq) {
        if (nq.prev != null)
            nq.prev.next = nq.next;
        if (nq.next != null)
            nq.next.prev = nq.prev;
        if (this.tail == nq)
            this.tail = nq.next;
    }
    
    public int get(int key) {
        Node n = map.get(key);
        if (n == null)
            return -1;
        oneStepUp(n);
        return n.value;
    }
    
    public void put(int key, int value) {
        if (capacity == 0)
            return;
        Node cn = map.get(key);
        if (cn != null) {
            cn.value = value;
            oneStepUp(cn);
            return;
        }
        if (map.size() == capacity) {
            map.remove(removeNode(this.tail.tail).key);
        }
        Node n = new Node(key, value); 
        if (this.tail == null) {
            NodeQueue nq = new NodeQueue(null, null, n, n);
            this.tail = nq;
            n.nq = nq;
        } 
        else if (this.tail.tail.freq == 0) {
            n.prev = this.tail.head;
            this.tail.head.next = n;
            n.nq = this.tail;
            this.tail.head = n;
        }
        else {
            NodeQueue nq = new NodeQueue(this.tail, null, n, n);
            this.tail.prev = nq;
            this.tail = nq;
            n.nq = nq;
        }
        map.put(key,n);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
