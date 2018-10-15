class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> res = new ArrayList<>();
        dfs(res,"",0,word);
        return res;
    }
    
    private void dfs(List<String> res, String curr, int start, String s) {
        res.add(curr + s.substring(start));
        if (start == s.length()) {
            return;
        }
        
        //New start position
        int i = 0;
        //Except first position, others need to start at the next position
        if (start > 0) {
            i = start + 1;
        }
        
        for (; i < s.length(); i++) {
            String prefix = curr + s.substring(start,i);
            //From ith character, change to numbers from 1 to s.length - i
            for (int j = 1; j <= s.length() - i; j++) {
                dfs(res, prefix + j, i + j, s);
            }
        }
    }
}
