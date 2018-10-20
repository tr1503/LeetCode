//Use priority queue(min heap) to convert this question to top K problem.
class Solution {
    class Worker {
        int quality;
        double ratio;
        Worker (int quality, double ratio) {
            this.quality = quality;
            this.ratio = ratio;
        }
    }
    
    public double mincostToHireWorkers(int[] quality, int[] wage, int K) {
        Worker[] w = new Worker[quality.length];
        for (int i = 0; i < quality.length; i++) {
            w[i] = new Worker(quality[i],(double) wage[i] / quality[i]);
        }
        Arrays.sort(w, (a,b) -> Double.compare(a.ratio,b.ratio));
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> Integer.compare(b,a));
        int minSum = 0;
        double min = Integer.MAX_VALUE;
        for (int i = 0; i < w.length; i++) {
            if (pq.size() < K - 1) {
                minSum += w[i].quality;
                pq.offer(w[i].quality);
            }
            else {
                min = Math.min(min, w[i].ratio * (minSum + w[i].quality));
                if (!pq.isEmpty() && pq.peek() > w[i].quality) {
                    minSum = minSum - pq.poll() + w[i].quality;
                    pq.offer(w[i].quality);
                }
            }
        }
        return min;
    }
}
