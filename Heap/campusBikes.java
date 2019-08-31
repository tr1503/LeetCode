// use priority queue (heap) to solve this question
// detail is at https://leetcode.com/problems/campus-bikes/discuss/305603/Java-Fully-Explained
// time is O(nlogn), space is O(n), n is the length of workers
class Solution {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        int n = workers.length;
        
        // priority order is distance, worker index, bike index
        PriorityQueue<int[]> queue = new PriorityQueue<int[]>((a, b) -> {
            int comp = Integer.compare(a[0], b[0]);
            if (comp == 0) {
                if (a[1] == b[1]) 
                    return Integer.compare(a[2], b[2]);
                return Integer.compare(a[1], b[1]);
            }
            return comp;
        });
        
        // loop through every possible pairs of bikes and workers
        // get the distance and put them to priority queue
        for (int i = 0; i < n; i++) {
            int[] worker = workers[i];
            for (int j = 0; j < bikes.length; j++) {
                int[] bike = bikes[j];
                int dist = Math.abs(bike[0] - worker[0]) + Math.abs(bike[1] - worker[1]);
                queue.add(new int[]{dist, i, j});
            }
        }
        
        // init the result array with unvisited value -1
        int[] res = new int[n];
        Arrays.fill(res, -1);
        
        // assign the bike to correct worker
        Set<Integer> bikeAssigned = new HashSet<>();
        while (bikeAssigned.size() < n) {
            int[] pair = queue.poll();
            if (res[pair[1]] == -1 && !bikeAssigned.contains(pair[2])) {
                res[pair[1]] = pair[2];
                bikeAssigned.add(pair[2]);
            }
        }
        return res;
    }
}
