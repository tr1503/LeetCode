class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        if ((pattern == null || pattern.length() == 0) && (str == null || str.length() == 0))
            return true;
        if ((pattern == null || pattern.length() == 0) || (str == null || str.length() == 0))
            return false;
        Map<Character,String> map1 = new HashMap<>();
        Map<String, Character> map2 = new HashMap<>();
        return helper(0,pattern,0,str,map1,map2);
    }
    
    private boolean helper(int p, String pattern, int s, String str, Map<Character,String> map1, Map<String, Character> map2) {
        if (p == pattern.length() && s == str.length())
            return true;
        if (p >= pattern.length() || s >= str.length())
            return false;
        char c = pattern.charAt(p);
        for (int i = s; i < str.length(); i++) {
            String curr = str.substring(s,i+1);
            if ((!map1.containsKey(c)) && (!map2.containsKey(curr))) {
                map1.put(c,curr);
                map2.put(curr,c);
                if (helper(p+1,pattern,i+1,str,map1,map2))
                    return true;
                map1.remove(c);
                map2.remove(curr);
            }
            else if (map1.containsKey(c) && map2.containsKey(curr)) {
                String word = map1.get(c);
                char ch = map2.get(curr);
                //IMPORTANT! if not equal, instead of returning false immediately 
                //We need to check other longer substrings
                if (!word.equals(curr) || ch != c)
                    continue;
                if (helper(p+1,pattern,i+1,str,map1,map2))
                    return true;
            }
        }
        return false;
    }
}
