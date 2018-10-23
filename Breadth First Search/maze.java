// Use bfs to finish this question, remember to create a visited 2d array to store
// and check if this node was visited.
class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        if (maze == null || maze.length == 0 || maze[0] == null || maze[0].length == 0)
            return true;
        int m = maze.length;
        int n = maze[0].length;
        boolean[][] visited = new boolean[m][n];
        int[][] dirs = new int[][]{{-1,0},{1,0},{0,-1},{0,1}};
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{start[0],start[1]});
        visited[start[0]][start[1]] = true;
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            if (curr[0] == destination[0] && curr[1] == destination[1])
                return true;
            for (int[] dir : dirs) {
                int x = curr[0];
                int y = curr[1];
                while (x >= 0 && y >= 0 && x < m && y < n && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                }
                // Meet the wall, back one position to change direction
                x -= dir[0];
                y -= dir[1];
                if (!visited[x][y]) {
                    visited[x][y] = true;
                    queue.offer(new int[]{x,y});
                }
            }
        }
        return false;
    }
}
