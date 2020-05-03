class BoundedBlockingQueue {
    
    private Queue<Integer> queue = new LinkedList<>();
    private int capacity;
    
    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;        
    }
    
    public void enqueue(int element) throws InterruptedException {
        synchronized(queue) {
            while (queue.size() == this.capacity)
                queue.wait();
            queue.offer(element);
            queue.notifyAll();
        }
    }
    
    public int dequeue() throws InterruptedException {
        synchronized(queue) {
            while (queue.size() == 0)
                queue.wait();
            int num = queue.poll();
            queue.notifyAll();
            return num;
        }
    }
    
    public int size() {
        return queue.size();
    }
}
