class Solution {
    class UnionFind {
        int count;
        int[] parent;
        int[] rank;
        
        public UnionFind(char[][] grid) {
            count = 0; // the result, # of connected components
            int m = grid.length;
            int n = grid[0].length;
            parent = new int[m * n];
            rank = new int[m * n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == '1') {
                        parent[i * n + j] = i * n + j;
                        count++;
                    }
                    rank[i * n + j] = 0;
                }
            }
        }
        
        public int find(int i) { // path compression
            if (parent[i] != i)
                parent[i] = find(parent[i]);
            return parent[i];
        }
        
        public void union(int x, int y) { // union with rank
            int rx = find(x);
            int ry = find(y);
            if (rx != ry) {
                if (rank[rx] > rank[ry])
                    parent[ry] = rx;
                else if (rank[rx] < rank[ry])
                    parent[rx] = ry;
                else {
                    parent[ry] = rx;
                    rank[rx] += 1;
                }
                count--;
            }
        }
        
        public int getCount() {
            return count;
        }
    }
    
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0)
            return 0;
        int m = grid.length;
        int n = grid[0].length;
        int num_islands = 0;
        UnionFind uf = new UnionFind(grid);
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1') {
                    grid[r][c] = '0';
                    if (r - 1 >= 0 && grid[r-1][c] == '1') {
                        uf.union(r * n + c, (r-1) * n + c);
                    }
                    if (r + 1 < m && grid[r+1][c] == '1') {
                        uf.union(r * n + c, (r+1) * n + c);
                    }
                    if (c - 1 >= 0 && grid[r][c-1] == '1') {
                        uf.union(r * n + c, r * n + c - 1);
                    }
                    if (c + 1 < n && grid[r][c+1] == '1') {
                        uf.union(r * n + c, r * n + c + 1);
                    }
                }
            }
        }
        return uf.getCount();
    }
}
