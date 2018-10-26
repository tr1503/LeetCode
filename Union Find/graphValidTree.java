// Use union find to solve this question. 
// After find two vertices between one edge, if their roots are same,
// it means they have cycle, return false. After checking if the graph has cycle,
// just check if each vertex has the connection with other vertex
class Solution {
    public boolean validTree(int n, int[][] edges) {
        int[] root = new int[n];
        Arrays.fill(root,-1);
        for (int[] edge : edges) {
            int x = find(root, edge[0]);
            int y = find(root, edge[1]);
            if (x == y)
                return false;
            root[x] = y;
        }
        return edges.length == n - 1;
    }
    
    private int find(int[] root, int i) {
        while (root[i] != -1)
            i = root[i];
        return i;
    }
}
