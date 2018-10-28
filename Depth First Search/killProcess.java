class Solution {
    private class Node {
        private Integer id;
        private List<Node> children;
        
        public Node(Integer id) {
            this.id = id;
            this.children = new ArrayList<>();
        }
    }
    
    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        HashMap<Integer,Node> map = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        for (Integer i : pid) {
            map.put(i, new Node(i));
        }
        for (int i = 0; i < ppid.size(); i++) {
            if (ppid.get(i) != 0) {
                // add all children to their parent
                map.get(ppid.get(i)).children.add(map.get(pid.get(i)));
            }
        }
        dfs(map.get(kill),res);
        return res;
    }
    
    private void dfs(Node node, List<Integer> res) {
        if (node == null)
            return;
        res.add(node.id);
        for (Node n : node.children) {
            dfs(n, res);
        }
    }
}
