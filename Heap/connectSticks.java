// Use priority queue to solve this problem
// time is O(nlogn), space is O(n)
class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int sum = 0;
        for (int stick : sticks) {
            pq.offer(stick);
        }
        while (pq.size() > 1) {
            int two = pq.poll() + pq.poll();
            sum += two;
            pq.offer(two);
        }
        return sum;
    }
}
