class Solution {
    public String minWindow(String s, String t) {
        int[] count = new int[128];
        for (char c: t.toCharArray()) {
            count[c]++;
        }
        int from = 0;
        int total = t.length();
        int min = Integer.MAX_VALUE;
        for (int i = 0, j = 0; i < s.length(); i++) {
            //Find the start point for sliding window
            if (count[s.charAt(i)]-- > 0)
                total--;
            //Once total = 0, the sliding window includes t
            while (total == 0) {
                if (i - j + 1 < min) {
                    min = i - j + 1;
                    from = j;
                }
                //Move j as a new from
                if (++count[s.charAt(j++)] > 0)
                    total++;
            }
        }
        return (min == Integer.MAX_VALUE) ? "" : s.substring(from,from + min);
    }
}
