class Solution {
    public String alienOrder(String[] words) {
        if (words == null || words.length == 0) 
            return "";
        Map<Character,Set<Character>> map = new HashMap<Character,Set<Character>>();
        Map<Character,Integer> degree = new HashMap<Character,Integer>();
        StringBuilder sb = new StringBuilder();
        
        //put all words in degree 0
        for (String s : words) {
            for (char c : s.toCharArray()) {
                degree.put(c,0);
            }
        }
        
        //compare with two words char by char
        //if different, since c1 is in front of c2, put c2 into c1's next set, c2's degree + 1
        for (int i = 0; i < words.length - 1; i++) {
            String curr = words[i];
            String next = words[i+1];
            int length = Math.min(curr.length(),next.length());
            for (int j = 0; j < length; j++) {
                char c1 = curr.charAt(j);
                char c2 = next.charAt(j);
                if (c1 != c2) {
                    Set<Character> set = map.getOrDefault(c1, new HashSet());
                    if (!set.contains(c2)) {
                        set.add(c2);
                        map.put(c1,set);
                        degree.put(c2,degree.get(c2) + 1);
                    }
                    break;
                }
            }
        }
        
        //topological sort by bfs
        Queue<Character> queue = new LinkedList<>();
        //put all 0 degree into queue, set extrance from 0
        for (char c : degree.keySet()) {
            if (degree.get(c) == 0)
                queue.offer(c);
        }
        
        while (!queue.isEmpty()) {
            char c = queue.poll();
            sb.append(c);
            if (map.containsKey(c)) {
                for (char ch : map.get(c)) {
                    //All next char's degree - 1
                    degree.put(ch,degree.get(ch) - 1);
                    if (degree.get(ch) == 0)
                        queue.offer(ch);
                }
            }
        }
        if (sb.length() != degree.size())
            return "";
        return sb.toString();
    }
}
