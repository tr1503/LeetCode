// Use union find to solve this question
// Label each element in the matrix, find the frinds of each element from union array root
class Solution {
    public int findCircleNum(int[][] M) {
        int n = M.length;
        int res = n;
        int[] root = new int[n];
        for (int i = 0; i < n; i++) {
            root[i] = i;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (M[i][j] == 1) {
                    int p1 = find(root,i);
                    int p2 = find(root,j);
                    if (p1 != p2) {
                        res--;
                        root[p2] = p1;
                    }
                }
            }
        }
        return res;
    }
    
    private int find(int[] root, int i) {
        while (i != root[i]) {
            root[i] = root[root[i]];
            i = root[i];
        }
        return i;
    }
}
