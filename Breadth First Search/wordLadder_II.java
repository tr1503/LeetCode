class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        HashSet<String> unvisted = new HashSet<>(wordList);
        HashSet<String> visited = new HashSet<>();
        List<List<String>> res = new ArrayList<>();
        HashMap<String,List<String>> map = new HashMap<>();
        if (wordList.size() == 0)
            return res;
        boolean found = false;
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
                    if (unvisted.contains(temp)) {
                        if (visited.add(temp)) {
                            next++;
                            queue.offer(temp);
                        }
                        if (map.containsKey(temp)) {
                            map.get(temp).add(word);
                        }
                        else {
                            List<String> list = new ArrayList<>();
                            list.add(word);
                            map.put(temp,list);
                        }
                        if (temp.equals(endWord))
                            found = true;
                    }
                }
            }
            if (curr == 0) {
                if (found) 
                    break;
                curr = next;
                next = 0;
                unvisted.removeAll(visited);
                visited.clear();
            }
        }
        dfs(res,new ArrayList<String>(), map, endWord, beginWord);
        return res;
    }
    
    private void dfs(List<List<String>> res, List<String> list, HashMap<String,List<String>> map, String word, String start) {
        if (word.equals(start)) {
            list.add(0, start);
            res.add(new ArrayList<>(list));
            list.remove(0);
            return;
        }
        list.add(0,word);
        if (map.get(word) != null) {
            for (String s : map.get(word)) {
                dfs(res,list,map,s,start);
            }
        }
        list.remove(0);
    }
}
