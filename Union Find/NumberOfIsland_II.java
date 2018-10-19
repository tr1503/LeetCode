//Use Union find with path compression, the time is O(klogmn).
//See https://www.cnblogs.com/yrbbest/p/5050749.html
class Solution {
    private int[] id;
    private int[] sz;
    private int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> res = new ArrayList<>();
        if (positions == null || positions.length == 0 || m < 0 || n < 0)
            return res;
        id = new int[m * n];
        sz = new int[m * n];
        for (int i = 0; i < id.length; i++) {
            id[i] = i;
        }
        int count = 0;
        for (int[] position : positions) {
            int p = position[0] * n + position[1];
            sz[p]++;
            count++;
            for (int[] direction : directions) {
                int newRow = position[0] + direction[0];
                int newCol = position[1] + direction[1];
                if (newRow < 0 || newCol < 0 || newRow > m - 1 || newCol > n - 1) {
                    continue;
                }
                int q = newRow * n + newCol;
                if (sz[q] > 0) {
                    if (isConnected(p,q))
                        continue;
                    else {
                        union(p,q);
                        count--;
                    }
                }
            }
            res.add(count);
        }
        return res;
    }
    
    private int find(int p) {
        while (p != id[p]) {
            id[p] = id[id[p]];
            p = id[p];
        }
        return p;
    }
    
    private boolean isConnected(int p,int q) {
        return find(p) == find(q);
    }
    
    private void union(int p, int q) {
        int up = find(p);
        int uq = find(q);
        if (up == uq) 
            return;
        else {
            if (sz[p] < sz[q]) {
                id[up] = uq;
                sz[q] += sz[p];
            }
            else {
                id[uq] = up;
                sz[p] += sz[q];
            }
        }
    }
}
