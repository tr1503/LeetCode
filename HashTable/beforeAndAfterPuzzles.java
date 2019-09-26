class Solution {
    public List<String> beforeAndAfterPuzzles(String[] phrases) {
        Map<String, Set<String>> head = new HashMap<>();
        Map<String, Set<String>> tail = new HashMap<>();
        Map<String, Integer> count = new HashMap<>();
        for (String p : phrases) {
            String[] words = p.split(" ");
            head.computeIfAbsent(words[0], s->new HashSet<>()).add(p);
            tail.computeIfAbsent(words[words.length - 1], s->new HashSet<>()).add(p);
            count.put(p, 1 + count.getOrDefault(p, 0));
        }
        TreeSet<String> res = new TreeSet<>();
        for (String end : tail.keySet()) {
            for (String p : head.getOrDefault(end, Collections.emptySet())) {
                for (String t : tail.get(end)) {
                    if (!t.equals(p) || count.get(p) > 1)
                        res.add(t + p.substring(end.length()));
                }
            }
        }
        return new ArrayList<>(res);
    }
}
