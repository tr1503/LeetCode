class Solution {
    HashMap<String, PriorityQueue<String>> map = new HashMap<>();
    List<String> res = new ArrayList<>();
    public List<String> findItinerary(String[][] tickets) {
        for (String[] ticket : tickets) {
            if (!map.containsKey(ticket[0])) {
                PriorityQueue<String> pq = new PriorityQueue<>();
                map.put(ticket[0],pq);
            }
            map.get(ticket[0]).offer(ticket[1]);
        }
        dfs("JFK");
        Collections.reverse(res);
        return res;
    }
    
    public void dfs(String s) {
        PriorityQueue<String> pq = map.get(s);
        while (pq != null && !pq.isEmpty()) {
            dfs(pq.poll());
        }
        res.add(s);
    }
}
