class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        Map<Character,Deque<String>> map = new HashMap<>();
        //Add each word to hashmap based on the first character
        for (char c = 'a'; c <= 'z'; c++) {
            map.putIfAbsent(c, new LinkedList<String>());
        }
        for (String word: words) {
            map.get(word.charAt(0)).addLast(word);
        }
        
        int count = 0;
        //Use each character's queue to iter S
        //if the length of word in this character's queue is 1, count + 1
        //otherwise, add its substring from the next to its new first character's queue
        for (char c : S.toCharArray()) {
            Deque<String> queue = map.get(c);
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String word = queue.removeFirst();
                if (word.length() == 1) {
                    count++;
                }
                else {
                    map.get(word.charAt(1)).addLast(word.substring(1));
                }
            }
        }
        return count;
    }
}
