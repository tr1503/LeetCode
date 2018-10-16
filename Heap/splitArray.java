class Solution {
    private HashMap<Integer,PriorityQueue<Integer>> map = new HashMap<>();
    
    public boolean isPossible(int[] nums) {
        for (int num: nums) {
            PriorityQueue<Integer> last = getOrPut(num - 1);
            int n = last.isEmpty() ? 0 : last.poll();
            PriorityQueue<Integer> curr = getOrPut(num);
            curr.offer(n + 1);
        }
        for (int key: map.keySet()) {
            for (int n : map.get(key)) {
                if (n < 3)
                    return false;
            }
        }
        return true;
    }
    
    private PriorityQueue<Integer> getOrPut(int num) {
        PriorityQueue<Integer> pq = map.get(num);
        if (pq == null) {
            pq = new PriorityQueue<Integer>();
            map.put(num,pq);
        }
        return pq;
    }
}
