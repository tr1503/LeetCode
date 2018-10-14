class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        HashSet<String> set = new HashSet<>(wordList);
        if (set.contains(beginWord))
            set.remove(beginWord);
        int level = 1;
        int curr = 1;
        int next = 0;
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        while (!queue.isEmpty()) {
            String word = queue.poll();
            curr--;
            for (int i = 0; i < word.length(); i++) {
                char[] wordUnit = word.toCharArray();
                for (char j = 'a'; j <= 'z'; j++) {
                    wordUnit[i] = j;
                    String temp = new String(wordUnit);
                    if (set.contains(temp)) {
                        if (temp.equals(endWord))
                            return level + 1;
                        next++;
                        queue.offer(temp);
                        set.remove(temp);
                    }
                }
            }
            if (curr == 0) {
                curr = next;
                next = 0;
                level++;
            }
        }
        return 0;
    }
}
