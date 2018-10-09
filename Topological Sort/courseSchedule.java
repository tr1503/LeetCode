//Use Toplogical Sort to solve this question
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        //Add all edges to graph
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<Integer>());
        }
        //(0,1), 0 is course, 1 is 0's prerequisite
        for (int i = 0; i < prerequisites.length; i++) {
            int course = prerequisites[i][0];
            int preq = prerequisites[i][1];
            graph.get(course).add(preq);
        }
        int[] visited = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (dfs(i,graph,visited))
                return false;
        }
        return true;
    }
    
    private boolean dfs(int curr, ArrayList<ArrayList<Integer>> graph, int[] visited) {
        //1 represents visiting, 2 represents visited
        //visiting means it could be cycle if its neighbor has a cycle with it
        //visited means this node does not need iter again
        if (visited[curr] == 1)
            return true;
        if (visited[curr] == 2)
            return false;
        visited[curr] = 1;
        for (int next : graph.get(curr)) {
            if (dfs(next,graph,visited))
                return true;
        }
        visited[curr] = 2;
        return false;
    }
}
