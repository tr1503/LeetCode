class AutocompleteSystem {
    private HashMap<String,Integer> map;
    private String curr;
    
    public AutocompleteSystem(String[] sentences, int[] times) {
        map = new HashMap<>();
        curr = "";
        for (int i = 0; i < sentences.length; i++) {
            map.put(sentences[i],times[i]);
        }
    }
    
    public List<String> input(char c) {
        List<String> res = new ArrayList<>();
        PriorityQueue<Map.Entry<String,Integer>> queue = new PriorityQueue(new Comparator<Map.Entry<String,Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                int count1 = o1.getValue();
                int count2 = o2.getValue();
                if (count1 < count2) 
                    return 1;
                else if (count1 > count2)
                    return -1;
                else {
                    String s1 = o1.getKey();
                    String s2 = o2.getKey();
                    return s1.compareTo(s2);
                }
            }
        });
        
        if (c == '#') {
            map.put(curr, map.getOrDefault(curr,0) + 1);
            curr = "";
            return new ArrayList<>();
        }
        
        curr += c;
        
        for (Map.Entry<String,Integer> entry : map.entrySet()) {
            String key = entry.getKey();
            if (key.startsWith(curr)) {
                queue.offer(entry);
            }
        }
        int count = 0;
        while (!queue.isEmpty() && count < 3) {
            Map.Entry<String, Integer> temp = queue.poll();
            res.add(temp.getKey());
            count++;
        }
        return res;
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */
