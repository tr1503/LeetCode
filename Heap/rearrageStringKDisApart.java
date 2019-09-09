class Pair {
    char ch;
    int cnt;
    Pair(char ch, int cnt) {
        this.ch = ch;
        this.cnt = cnt;
    }
}

class Solution {
    public String rearrangeString(String s, int k) {
        if (k == 0)
            return s;
        int n = s.length();
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            int count = 1;
            if (map.containsKey(ch)) {
                count = map.get(ch) + 1;
            }
            map.put(ch, count);
        }
        
        PriorityQueue<Pair> pq = new PriorityQueue<>(10, new Comparator<Pair>() {
            @Override
            public int compare(Pair p1, Pair p2) {
                if (p1.cnt != p2.cnt)
                    return p2.cnt - p1.cnt;
                else
                    return p2.ch - p1.ch;
            }
        });
        
        // build priority queue to order the char based on frequency
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            pq.offer(new Pair(entry.getKey(), entry.getValue()));
        }
        
        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            List<Pair> temp = new ArrayList<>(); // temp array to avoid picking up same char in one k-segment
            int d = Math.min(k, n);
            for (int i = 0; i < d; i++) {
                if (pq.isEmpty())
                    return "";
                Pair pair = pq.poll();
                sb.append(pair.ch);
                if (--pair.cnt > 0) 
                    temp.add(pair);
                n--;
            }
            for (Pair p : temp) {
                pq.offer(p);
            }
        }
        return sb.toString();
    }
}
