class Solution {
    public String predictPartyVictory(String senate) {
        int n = senate.length();
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (senate.charAt(i) == 'R')
                q1.offer(i);
            else
                q2.offer(i);
        }
        while (!q1.isEmpty() && !q2.isEmpty()) {
            int i = q1.poll();
            int j = q2.poll();
            if (i < j)
                q1.offer(i + n);
            else
                q2.offer(j + n);
        }
        return (q1.size() > q2.size()) ? "Radiant" : "Dire";
    }
}
