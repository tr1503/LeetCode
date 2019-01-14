class Solution {
    public String replaceWords(List<String> dict, String sentence) {
        String[] tokens = sentence.split(" ");
        TrieNode trie = buildTrie(dict);
        return replaceWords(tokens, trie);
    }
    
    private String replaceWords(String[] tokens, TrieNode root) {
        StringBuilder sb = new StringBuilder();
        for (String token : tokens) {
            sb.append(getShortestWord(token, root));
            sb.append(" ");
        }
        return sb.substring(0, sb.length() - 1);
    }
    
    private String getShortestWord(String token, final TrieNode root) {
        TrieNode curr = root;
        StringBuilder sb = new StringBuilder();
        for (char c : token.toCharArray()) {
            sb.append(c);
            if (curr.children[c - 'a'] != null) {
                if (curr.children[c - 'a'].isWord)
                    return sb.toString();
                curr = curr.children[c - 'a'];
            }
            else {
                return token;
            }
        }
        return token;
    }
    
    private TrieNode buildTrie(List<String> dict) {
        TrieNode root = new TrieNode(' ');
        for (String word : dict) {
            TrieNode curr = root;
            for (char c : word.toCharArray()) {
                if (curr.children[c - 'a'] == null) 
                    curr.children[c - 'a'] = new TrieNode(c);
                curr = curr.children[c - 'a'];
            }
            curr.isWord = true;
        }
        return root;
    }
    public class TrieNode {
        char val;
        TrieNode[] children;
        boolean isWord;
        
        public TrieNode(char val) {
            this.val = val;
            this.children = new TrieNode[26];
            this.isWord = false;
        }
    }
}
