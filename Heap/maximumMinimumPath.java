class Unit {
    public int value;
    public int row;
    public int col;
    public Unit(int value, int i, int j) {
        this.value = value;
        this.row = i;
        this.col = j;
    }
}

class Solution {
    public int maximumMinimumPath(int[][] A) {
        int n = A.length;
        int m = A[0].length;
        int min = Math.min(A[n-1][m-1], A[0][0]);
        
        PriorityQueue<Unit> pq = new PriorityQueue<>((a,b)-> b.value - a.value);
        int[][] visited = new int[n][m];
        int i = 0;
        int j = 0;
        while (i != n - 1 || j != m - 1) {
            visited[i][j] = 1;
            int curr = A[i][j];
            if (i - 1 >= 0 && visited[i-1][j] == 0) {
                visited[i-1][j] = 1;
                pq.offer(new Unit(A[i-1][j], i-1, j));
            }
            
            if (i + 1 < n && visited[i+1][j] == 0) {
                if (reach(i + 1, j, n, m))
                    return min;
                visited[i+1][j] = 1;
                pq.offer(new Unit(A[i+1][j], i+1, j));
            }
            
            if (j - 1 >= 0 && visited[i][j-1] == 0) {
                visited[i][j-1] = 1;
                pq.offer(new Unit(A[i][j-1], i, j-1));
            }
            
            if (j + 1 < m && visited[i][j+1] == 0) {
                if (reach(i, j + 1, n, m))
                    return min;
                visited[i][j+1] = 1;
                pq.offer(new Unit(A[i][j+1], i, j+1));
            }
            Unit next = pq.poll();
            if (next.value < min)
                min = next.value;
            i = next.row;
            j = next.col;
        }
        
        return min;
    }
    
    public boolean reach(int i, int j, int n, int m) {
        if (i == n - 1 && j == m - 1)
            return true;
        return false;
    }
}
