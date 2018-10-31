class Solution {
    public String findLongestWord(String s, List<String> d) {
        //Sort all strings in dictionary by the length from long to short
        //if lengths are same, use the lexicographical order 
        Collections.sort(d, (a,b) -> a.length() != b.length()? b.length() - a.length() : a.compareTo(b));
        char[] arr = s.toCharArray();
        for (String word : d) {
            int i = 0;
            for (char c : arr) {
                if (c == word.charAt(i))
                    i++;
                if (i == word.length())
                    return word;
            }
        }
        return "";
        
        // Without using sort, time is O(nk), k is the average length of words in dictionary
        String res = "";
        for (String word : d) {
            int i = 0;
            for (char c : s.toCharArray()) {
                if (i < word.length() && c == word.charAt(i))
                    i++;
            }
            if (i == word.length() && word.length() >= res.length()) {
                    if (word.length() > res.length() || word.compareTo(res) < 0)
                        res = word;
            }
        }
        return res;
    }
}
