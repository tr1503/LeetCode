//Use bfs with bit manipulation to finish the question
class Solution {
    public int shortestPathLength(int[][] graph) {
        int kAns = (1 << graph.length) - 1;
        Queue<int[]> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        for (int i = 0; i < graph.length; i++) {
            queue.offer(new int[]{i,1<<i});
        }
        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] p = queue.peek();
                queue.poll();
                int node = p[0];
                int state = p[1];
                if (state == kAns) 
                    return steps;
                int key = (node << 16) | state;
                if (visited.contains(key))
                    continue;
                visited.add(key);
                for (int next : graph[node]) {
                    queue.offer(new int[]{next, state | (1 << next)});
                }
            }
            steps++;
        }
        return -1;
    }
}
