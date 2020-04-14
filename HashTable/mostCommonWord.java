class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> ban = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> count = new HashMap<>();
        String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split("\\s+");
        for (String w : words) {
            if (!ban.contains(w)) 
                count.put(w, count.getOrDefault(w, 0) + 1);
        }
        int max = 0;
        String res = "";
        for (String w : count.keySet()) {
            if (count.get(w) > max) {
                max = count.get(w);
                res = w;
            }
        }
        return res;
    }
}
