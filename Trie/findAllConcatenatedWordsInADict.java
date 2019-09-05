// Use trie to solve this problem, detail is at https://leetcode.com/problems/concatenated-words/discuss/95644/102ms-java-Trie-%2B-DFS-solution.-With-explanation-easy-to-understand.
// time is O(n * k), n is the size of words, k is the length of each word, space is O(n)
class TrieNode {
    TrieNode[] sons;
    boolean isEnd;
    public TrieNode() {
        sons = new TrieNode[26];
    }
}

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> res = new ArrayList<String>();
        if (words == null || words.length == 0)
            return res;
        TrieNode root = new TrieNode();
        for (String word : words) { // construct the trie tree
            if (word.length() == 0)  
                continue;
            addWord(word, root);
        }
        for (String word : words) { // check word is concatenated word
            if (word.length() == 0) 
                continue;
            if (testWord(word.toCharArray(), 0, root, 0)) 
                res.add(word);
        }
        return res;
    }
    
    public boolean testWord(char[] chars, int index, TrieNode root, int count) {
        TrieNode curr = root;
        int n = chars.length;
        for (int i = index; i < n; i++) {
            if (curr.sons[chars[i] - 'a'] == null) {
                return false;
            }
            if (curr.sons[chars[i] - 'a'].isEnd) {
                if (i == n - 1) {
                    return count >= 1;
                }
                if (testWord(chars, i + 1, root, count + 1)) {
                    return true;
                }
            }
            curr = curr.sons[chars[i] - 'a'];
        }
        return false;
    }
    
    public void addWord(String str, TrieNode root) {
        char[] chars = str.toCharArray();
        TrieNode curr = root;
        for (char c : chars) {
            if (curr.sons[c - 'a'] == null) {
                curr.sons[c - 'a'] = new TrieNode();
            }
            curr = curr.sons[c - 'a'];
        }
        curr.isEnd = true;
    }
}
