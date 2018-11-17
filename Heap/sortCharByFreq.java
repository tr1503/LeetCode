class Solution {
    private class Counter {
        char c;
        int count;
        public Counter(char c, int count) {
            this.c = c;
            this.count = count;
        }
    }
    
    public String frequencySort(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!map.containsKey(s.charAt(i)))
                map.put(s.charAt(i),1);
            else
                map.put(s.charAt(i),map.get(s.charAt(i)) + 1);
        }
        PriorityQueue<Counter> pq = new PriorityQueue<>(10, new Comparator<Counter>() {
            @Override
            public int compare(Counter o1, Counter o2) {
                if (o1.count > o2.count)
                    return -1;
                else if (o1.count < o2.count)
                    return 1;
                else
                    return 0;
            }
        });
        for (char c : map.keySet()) {
            Counter counter = new Counter(c,map.get(c));
            pq.offer(counter);
        }
        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            Counter curr = pq.poll();
            for (int i = 0; i < curr.count; i++) {
                sb.append(curr.c);
            }
        }
        return sb.toString();
    }
}
