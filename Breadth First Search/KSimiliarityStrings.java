class Solution {
    public int kSimilarity(String A, String B) {
        if (A.equals(B))
            return 0;
        Set<String> visited = new HashSet<>();
        Queue<String > queue = new LinkedList<>();
        queue.offer(A);
        visited.add(A);
        int res = 0;
        while (!queue.isEmpty()) {
            res++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String s = queue.poll();
                int j = 0;
                while (s.charAt(j) == B.charAt(j))
                    j++;
                for (int k = j + 1; k < s.length(); k++) {
                    if (s.charAt(k) == B.charAt(k) || s.charAt(j) != B.charAt(k))
                        continue;
                    String temp = swap(s, j, k);
                    if (temp.equals(B))
                        return res;
                    if (visited.add(temp))
                        queue.add(temp);
                }
            }
        }
        return res;
    }
    
    private String swap(String s, int i, int j) {
        char[] ca = s.toCharArray();
        char temp = ca[i];
        ca[i] = ca[j];
        ca[j] = temp;
        return new String(ca);
    }
}
