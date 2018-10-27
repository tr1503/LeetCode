// use priority queue (heap) to solve this question
// use a max heap to store the height of current building
// the top of heap is the max height of all recent buildings
// if e1.x == e2.x, it means it has overlapping on skyline, so we need to check different siutations.
class Edge {
    int height;
    int x;
    boolean isStart;
    
    Edge(int x, int height, boolean isStart) {
        this.x = x;
        this.height = height;
        this.isStart = isStart;
    }
}

class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> res = new ArrayList<>();
        if (buildings == null || buildings.length == 0 || buildings[0].length == 0)
            return res;
        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < buildings.length; i++) {
            edges.add(new Edge(buildings[i][0],buildings[i][2],true));
            edges.add(new Edge(buildings[i][1],buildings[i][2],false));
        }
        
        Collections.sort(edges, new Comparator<Edge>() {
            public int compare(Edge e1, Edge e2) {
                if (e1.x != e2.x)
                    return e1.x - e2.x;
                // e1 and e2 are both start, choose the higher one
                else if (e1.isStart && e2.isStart)
                    return e2.height - e1.height;
                // e1 and e2 are both end, choose the lower one
                else if (!e1.isStart && !e2.isStart)
                    return e1.height - e2.height;
                // if e1 and e2 are on different side, check which one is start
                // put the start one first
                else 
                    return e1.isStart ? -1 : 1;
            }
        });
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(10, new Comparator<Integer>() {
            public int compare(Integer e1, Integer e2) {
                return e2.compareTo(e1);
            }
        });
        
        for (Edge edge : edges) {
            if (edge.isStart) {
                if (pq.isEmpty() || edge.height > pq.peek()) {
                    res.add(new int[]{edge.x, edge.height});
                }
                pq.offer(edge.height);
            }
            else {
                pq.remove(edge.height);
                if (pq.isEmpty()) {
                    res.add(new int[]{edge.x,0});
                }
                else if (edge.height > pq.peek()) {
                    res.add(new int[]{edge.x, pq.peek()});
                }
            }
        }
        return res;
    }
}
