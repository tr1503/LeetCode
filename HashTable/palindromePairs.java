class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (words == null || words.length == 0)
            return res;
        //Build a hashmap for String: its index in array
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            map.put(words[i],i);
        }
        //Case 1: "" can be combined with any palindrome
        if (map.containsKey("")) {
            int index = map.get("");
            for (int i = 0; i < words.length; i++) {
                if (i == index)
                    continue;
                if (isPalindrome(words[i])) {
                    res.add(Arrays.asList(i,index));
                    res.add(Arrays.asList(index,i));
                }
            }
        }
        //Case 2: one string's reverse string is other string in array
        for (int i = 0; i < words.length; i++) {
            String curr = reverse(words[i]);
            if (map.containsKey(curr)) {
                int index = map.get(curr);
                if (index == i) 
                    continue;
                res.add(Arrays.asList(i,index));
            }
        }
        
        //Case 3: s1[0: cut] is palindrome and s1[cur+1:] = reverse(s2) => (s2,s1)
        //Case 4: s1[cut+1:] is palindrome and s1[0: cut] = reverse(s2) => (s1,s2)
        for (int i = 0; i < words.length; i++) {
            String curr = words[i];
            for (int cut = 1; cut < curr.length(); cut++) {
                if (isPalindrome(curr.substring(0,cut))) {
                    String rev = reverse(curr.substring(cut));
                    if (map.containsKey(rev)) {
                        int index = map.get(rev);
                        if (index == i) continue;
                        res.add(Arrays.asList(index,i));
                    }
                }
                if (isPalindrome(curr.substring(cut))) {
                    String rev = reverse(curr.substring(0,cut));
                    if (map.containsKey(rev)) {
                        int index = map.get(rev);
                        if (index == i) continue;
                        res.add(Arrays.asList(i,index));
                    }
                }
            }
        }
        return res;
    }
    
    private String reverse(String str) {
        StringBuilder sb = new StringBuilder(str);
        return sb.reverse().toString();
    }
    
    private boolean isPalindrome(String word) {
        for (int i = 0, j = word.length()-1; i<j; i++,j--) {
            if (word.charAt(i) == word.charAt(j))
                continue;
            else
                return false;
        }
        return true;
    }
}
