// Use dfs and color fill algorithm to solve this question
// Set each element as no color firstly and recursive traversal each vertex
// If this element's correct color is same as what color we will fill, return true
// Recursive traversal the neighbors of each vertex with different color
// If one neighbor vertex can't use this different color, return false
class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] colors = new int[graph.length];
        for (int i = 0; i < graph.length; i++) {
            if (colors[i] == 0 && !valid(graph, 1, i, colors))
                return false;
        }
        return true;
    }
    
    private boolean valid(int[][] graph, int color, int curr, int[] colors) {
        if (colors[curr] != 0)
            return colors[curr] == color;
        colors[curr] = color;
        for (int i : graph[curr]) {
            if (!valid(graph, -1 * color, i, colors)) {
                return false;
            }
        }
        return true;
    }
}
