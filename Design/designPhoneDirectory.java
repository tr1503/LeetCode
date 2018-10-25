class PhoneDirectory {

    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    Queue<Integer> queue;
    Set<Integer> set;
    public PhoneDirectory(int maxNumbers) {
        this.queue = new LinkedList<>();
        this.set = new HashSet<>();
        for (int i = 0; i < maxNumbers; i++) {
            this.queue.offer(i);
            this.set.add(i);
        }
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if (this.queue.isEmpty()) {
            return -1;
        }
        int t = this.queue.peek();
        this.set.remove(t);
        return this.queue.poll();
    }
    
    /** Check if a number is available or not. */
    public boolean check(int number) {
        return this.set.contains(number);
    }
    
    /** Recycle or release a number. */
    public void release(int number) {
        if (!this.set.contains(number)) {
            this.queue.offer(number);
            this.set.add(number);
        }   
    }
}

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * boolean param_2 = obj.check(number);
 * obj.release(number);
 */
