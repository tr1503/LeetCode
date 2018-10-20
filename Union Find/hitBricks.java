class Solution {
    private static final int[][] dirs = new int[][] {{0,-1},{0,1},{-1,0},{1,0}};
    public int[] hitBricks(int[][] grid, int[][] hits) {
        int[] res = new int[hits.length];
        int rows = grid.length;
        int cols = grid[0].length;
        UnionFind uf = new UnionFind(rows * cols + 1);
        
        //hits
        for (int i = 0; i < hits.length; i++) {
            grid[hits[i][0]][hits[i][1]]--;
        }
        
        //build the board (after all hits)
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                //if the current cell is a brick, we can union it with its neighbors
                if (grid[i][j] == 1) {
                    int pos = i * cols + j;
                    //if it is on the roof, it will stay in the board
                    //so we union it with the root
                    if (i == 0)
                        uf.union(pos, rows * cols);
                    //Only union the left and up grid of current position
                    if (i > 0 && grid[i - 1][j] == 1)
                        uf.union(pos, (i-1) * cols + j);
                    if (j > 0 && grid[i][j-1] == 1)
                        uf.union(pos, i * cols + j - 1);
                }
            }
        }
        
        //reverse the time
        for (int i = hits.length - 1; i >= 0; i--) {
            int hitRow = hits[i][0];
            int hitCol = hits[i][1];
            //recover the empty bricks
            if (grid[hitRow][hitCol] == -1) {
                grid[hitRow][hitCol] = 0;
                continue;
            }
            
            //get how many bricks in the board currently
            int preRoof = uf.getRoof();
            for (int[] dir : dirs) {
                int nextRow = hitRow + dir[0];
                int nextCol = hitCol + dir[1];
                if (nextRow < 0 || nextCol < 0 || nextRow >= rows || nextCol >= cols || grid[nextRow][nextCol] != 1) 
                    continue;
                uf.union(hitRow * cols + hitCol, nextRow * cols + nextCol);
            }
            //if the hit position is in 0th row, it should be union to root (rows * cols)
            if (hitRow == 0)
                uf.union(hitRow * cols + hitCol, rows * cols);
            //add the hit brick
            grid[hitRow][hitCol] = 1;
            res[i] = Math.max(0, uf.getRoof() - preRoof - 1);
        }
        return res;
    }
    
    class UnionFind {
        int[] parent, rank;
        
        UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 1;
            }
            rank[n-1] = 0;
        }
        
        public int find(int i) {
            if (i != parent[i]) {
                parent[i] = find(parent[i]);
            }
            return parent[i];
        }
        
        public void union(int u, int v) {
            int pu = find(u);
            int pv = find(v);
            if (pu == pv) 
                return;
            else if (pu > pv) {
                //make pv becomes the bigger one
                int temp = pu;
                pu = pv;
                pv = temp;
            }
            
            //Union smaller to bigger, unless pv is root
            if (pv == rank.length - 1) {
                parent[pu] = pv;
                rank[pv] += rank[pu];
            }
            else {
                parent[pv] = pu;
                rank[pu] += rank[pv];
            }
        }
        
        //return how many bricks can stay in the board
        public int getRoof() {
            return rank[rank.length - 1];
        }
    }
}
