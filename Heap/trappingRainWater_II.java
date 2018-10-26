class Cell {
    public int x, y, h;
    public Cell() {}
    
    public Cell(int x, int y, int h) {
        this.x = x;
        this.y = y;
        this.h = h;
    }
}

// use min-heap (priority queue in java) and bfs four directions for each element to solve this question
// get the result from outer ot inner
class Solution {
    public int trapRainWater(int[][] heightMap) {
        if (heightMap == null || heightMap.length == 0 || heightMap[0].length == 0)
            return 0;
        int m = heightMap.length;
        int n = heightMap[0].length;
        boolean[][] visited = new boolean[m][n];
        int[] dirX = new int[]{0,0,-1,1};
        int[] dirY = new int[]{-1,1,0,0};
        // initlize the min heap, based on the height of each cell
        PriorityQueue<Cell> minheap = new PriorityQueue<Cell>(1, new Comparator<Cell>() {
            public int compare(Cell o1, Cell o2) {
                if (o1.h > o2.h)
                    return 1;
                else if (o1.h < o2.h)
                    return -1;
                else
                    return 0;
            }
        });
        // traversal the outer cells, add them to minheap
        for (int i = 0; i < m; i++) {
            minheap.offer(new Cell(i,0,heightMap[i][0]));
            minheap.offer(new Cell(i,n-1,heightMap[i][n-1]));
            visited[i][0] = true;
            visited[i][n-1] = true;
        }
        
        for (int j = 0; j < n; j++) {
            minheap.offer(new Cell(0,j,heightMap[0][j]));
            minheap.offer(new Cell(m-1,j,heightMap[m-1][j]));
            visited[0][j] = true;
            visited[m-1][j] = true;
        }
        int water = 0;
        // start from the min heap cell (from outer), check 4 directions
        while (!minheap.isEmpty()) {
            Cell curr = minheap.poll();
            for (int k = 0; k < 4; k++) {
                int x = curr.x + dirX[k];
                int y = curr.y + dirY[k];
                if (x >= 0 && y >= 0 && x < m && y < n && !visited[x][y]) {
                    minheap.offer(new Cell(x, y, Math.max(curr.h, heightMap[x][y])));
                    visited[x][y] = true;
                    // fill in water or not
                    water += Math.max(0, curr.h - heightMap[x][y]);
                }
            }
        }
        return water;
    }
}
