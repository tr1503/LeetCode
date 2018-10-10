//Use dfs and hash map to finish this question
class Solution {
    HashMap<Integer, List<String>> map = new HashMap<>();
    
    public List<String> wordBreak(String s, List<String> wordDict) {
        return dfs(s,wordDict,0);
    }
    
    private List<String> dfs(String s, List<String> wordDict, int start) {
        if (map.containsKey(start)) {
            return map.get(start);
        }
        List<String> res = new ArrayList<>();
        if (start == s.length()) {
            res.add("");
        }
        for (int end = start+1; end <= s.length(); end++) {
            if (wordDict.contains(s.substring(start,end))) {
                List<String> list = dfs(s,wordDict,end);
                for (String word: list) {
                    res.add(s.substring(start,end) + (word.equals("") ? "": " ") + word);
                }
            }
        }
        map.put(start,res);
        return res;
    }
}
