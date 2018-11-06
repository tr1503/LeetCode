// Use dfs to update each value in the maze. If current element's value is more than the current
// depth, we can set current element's value to this depth and dfs four directions.
// Finally, we can use the current depth to update each element in the maze.
class Solution {
    public void wallsAndGates(int[][] rooms) {
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[i].length; j++) {
                if (rooms[i][j] == 0)
                    dfs(rooms, i, j, 0);
            }
        }   
    }
    
    private void dfs(int[][] rooms, int i, int j, int val) {
        if (i < 0 || i >= rooms.length || j < 0 || j >= rooms[i].length || rooms[i][j] < val)
            return;
        rooms[i][j] = val;
        dfs(rooms, i+1, j, val + 1);
        dfs(rooms, i-1, j, val + 1);
        dfs(rooms, i, j+1, val + 1);
        dfs(rooms, i, j-1, val + 1);
    }
}
