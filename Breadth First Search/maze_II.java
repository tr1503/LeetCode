class Solution {
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int m = maze.length;
        int n = maze[0].length;
        // Create a 2d array to store each distances from start to this position
        // The return result should be the value at the destination position
        int[][] dists = new int[m][n];
        for (int[] row : dists) {
            Arrays.fill(row,Integer.MAX_VALUE);
        }
        int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{start[0],start[1]});
        dists[start[0]][start[1]] = 0;
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            for (int[] dir : dirs) {
                int x = curr[0];
                int y = curr[1];
                int dist = dists[curr[0]][curr[1]];
                while (x >= 0 && y >= 0 && x < m && y < n && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                    dist++;
                }
                // Meet the wall, go back one
                x -= dir[0];
                y -= dir[1];
                dist--;
                if (dists[x][y] > dist) {
                    dists[x][y] = dist;
                    if (x != destination[0] || y != destination[1])
                        queue.offer(new int[]{x,y});
                }
            }
        }
        int res = dists[destination[0]][destination[1]];
        return (res == Integer.MAX_VALUE) ? -1 : res;
    }
}
