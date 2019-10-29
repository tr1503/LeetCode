class Solution {
    public int openLock(String[] deadends, String target) {
        String start = "0000";
        Set<String> dead = new HashSet<>();
        for (String d : deadends) {
            dead.add(d);
        }
        if (dead.contains(start))
            return -1;
        
        Queue<String> queue = new LinkedList<>();
        queue.offer(start);
        Set<String> visited = new HashSet<>();
        visited.add(start);
        int steps = 0;
        
        while (!queue.isEmpty()) {
            steps++;
            int size = queue.size();
            for (int s = 0; s < size; s++) {
                String node = queue.poll();
                for (int i = 0; i < 4; i++) {
                    for (int j = -1; j <= 1; j += 2) {
                        char[] chars = node.toCharArray();
                        chars[i] = (char)(((chars[i] - '0') + j + 10) % 10 + '0');
                        String next = new String(chars);
                        if (next.equals(target))
                            return steps;
                        if (dead.contains(next) || visited.contains(next))
                            continue;
                        visited.add(next);
                        queue.offer(next);
                    }
                }
            }
        }
        return -1;
    }
}
