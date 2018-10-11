class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int[] can1 = new int[] {-1,-1};
        int[] can2 = new int[] {-1,-1};
        int[] root = new int[edges.length + 1];
        for (int[] edge : edges) {
            if (root[edge[1]] == 0) {
                root[edge[1]] = edge[0];
            }
            else {
                can2 = new int[] {edge[0],edge[1]};
                //Get the previous this node and its parent
                can1 = new int[] {root[edge[1]],edge[1]};
                edge[1] = 0;
            }
        }
        for (int i = 0; i < root.length; i++) {
            root[i] = i;
        }
        for (int[] edge : edges) {
            if (edge[1] == 0)
                continue;
            //Use union find to find the edge constructs a cycle
            if (find(root,edge[0]) == edge[1]) {
                if (can1[0] == -1)
                    return edge;
                else
                    return can1;
            }
            root[edge[1]] = edge[0];
        }
        return can2;
    }
    
    private int find(int[] root, int p) {
        while (root[p] != p) {
            root[p] = root[root[p]];
            p = root[p];
        }
        return p;
    }
}
