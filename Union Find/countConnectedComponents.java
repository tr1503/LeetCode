// Use union find to solve this question
// After union find, two connected nodes should have same root value, 
// Unconnected nodes don't have same value and then result should decrease
class Solution {
    public int countComponents(int n, int[][] edges) {
        int res = n;
        int[] root = new int[n];
        for (int i = 0; i < n; i++) {
            root[i] = i;
        }
        for (int[] edge : edges) {
            int x = find(root, edge[0]);
            int y = find(root, edge[1]);
            if (x != y) {
                res--;
                // prevent repeating iter
                root[y] = x;
            }
        }
        return res;
    }
    
    private int find(int[] root, int i) {
        while (root[i] != i)
            i = root[i];
        return i;
    }
}
