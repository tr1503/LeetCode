// Use bfs to solve this problem and details is at https://zhuanlan.zhihu.com/p/45339906
// time is O(n), space is O(n)
class Solution {
    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        if (n == 1)
            return 0;
        int step = 0;
        boolean[] visited = new boolean[n*n];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        visited[0] = true;
        while (!queue.isEmpty()) {
            step++;
            int size = queue.size();
            while (size-- > 0) {
                int pos = queue.poll();
                for (int i = 1; i <= 6; i++) {
                    int next = pos + i;
                    if (next == n * n) {
                        return step;
                    }
                    int nr = getrow(next, n);
                    int nc = getcol(next, n);
                    if (board[nr][nc] != -1) {
                        next = board[nr][nc];
                        if (next == n * n) 
                            return step;
                        nr = getrow(next, n);
                        nc = getcol(next, n);
                    }
                    
                    if (!visited[next - 1]) {
                        queue.add(next);
                        visited[next - 1] = true;
                    }
                }
            }
        }
        return -1;
    }
    
    public int getrow(int v, int n) {
        return n - 1 - (v - 1) / n;
    }
    
    public int getcol(int v, int n) {
        return (((v-1)/n) % 2 == 0) ? ((v - 1) % n) : (n - 1 - (v - 1) % n);
    }
}
