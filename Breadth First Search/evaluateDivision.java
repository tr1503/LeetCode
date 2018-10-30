// use queue to implement bfs for this question
class Solution {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < equations.length; i++) {
            // add arcs for each direction
            addArc(graph,equations[i][0],equations[i][1],values[i]);
            addArc(graph,equations[i][1],equations[i][0],1 / values[i]);
        }
        double[] res = new double[queries.length];
        for (int i = 0; i < res.length; i++) {
            res[i] = getValue(graph,queries[i][0],queries[i][1]);
        }
        return res;
    }
    
    private void addArc(Map<String, Map<String, Double>> graph, String u, String v, double value) {
        Map<String, Double> arcMap;
        if (graph.containsKey(u)) {
            arcMap = graph.get(u);
        }
        else {
            arcMap = new HashMap<>();
        }
        arcMap.put(v, value);
        graph.put(u,arcMap);
    }
    
    private double getValue(Map<String, Map<String, Double>> graph, String u, String v) {
        if (graph.get(u) == null || graph.get(v) == null)
            return -1;
        Queue<String> queue = new LinkedList<>();
        // divide value of u
        Map<String, Double> value = new HashMap<>();
        // check if the vertex has been in the queue
        Set<String> validation = new HashSet<>();
        queue.offer(u);
        validation.add(u);
        value.put(u,1.0);
        String curr, next;
        while (!queue.isEmpty()) {
            curr = queue.poll();
            for (Map.Entry<String, Double> arc : graph.get(curr).entrySet()) {
                next = arc.getKey();
                value.put(next, value.get(curr) * arc.getValue());
                if (next.equals(v)) {
                    return value.get(v);
                }
                else if (!validation.contains(next)) {
                    queue.offer(next);
                    validation.add(next);
                }
            }
        }
        return -1.0;
    }
}
