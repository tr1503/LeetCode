class Solution {
    class Point implements Comparable<Point> {
        int x, y, dist;
        String path;
        
        public Point(int x, int y, int dist, String path) {
            this.x = x;
            this.y = y;
            this.dist = dist;
            this.path = path;
        }
        
        public int compareTo(Point point) {
            if (this.dist != point.dist)
                return this.dist - point.dist;
            return this.path.compareTo(point.path);
        }
    }
    
    private static int[][] dirs = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
    private static char[] ways = {'d', 'l', 'r', 'u'};
    
    public String findShortestWay(int[][] maze, int[] ball, int[] hole) {
        int m = maze.length;
        int n = maze[0].length;
        boolean[][] visited = new boolean[m][n];
        PriorityQueue<Point> pq = new PriorityQueue<>();
        pq.add(new Point(ball[0],ball[1],0,""));
        
        while (!pq.isEmpty()) {
            Point curr = pq.poll();
            if (curr.x == hole[0] && curr.y == hole[1])
                return curr.path;
            if (!visited[curr.x][curr.y]) {
                visited[curr.x][curr.y] = true;
                for (int i = 0; i < 4; i++) {
                    Point next = moveForward(maze,curr,i,hole);
                    pq.add(new Point(next.x,next.y,next.dist,next.path + ways[i]));
                }
            }
        }
        return "impossible";
    }
    
    private Point moveForward(int[][] maze, Point curr, int direction, int[] hole) {
        int m = maze.length;
        int n = maze[0].length;
        int x = curr.x;
        int y = curr.y;
        int dist = curr.dist;
        String path = curr.path;
        while (x >= 0 && y >= 0 && x < m && y < n && maze[x][y] == 0) {
            x += dirs[direction][0];
            y += dirs[direction][1];
            dist++;
            if (x == hole[0] && y == hole[1]) {
                return new Point(x,y,dist,path);
            }
        }
        x -= dirs[direction][0];
        y -= dirs[direction][1];
        dist--;
        return new Point(x,y,dist,path);
    }
}
