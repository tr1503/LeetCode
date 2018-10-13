class Solution {
    public String removeDuplicateLetters(String s) {
        int[] freqs = new int[256];
        for (int i = 0; i < s.length(); i++) {
            freqs[s.charAt(i)]++;
        }
        //To store if this char was visited
        boolean[] visited = new boolean[256];
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            freqs[c]--;
            if (visited[c]) 
                continue;
            //pop all characters that are larger than current character and will appear in the rest of string
            while (!stack.isEmpty() && stack.peek() > c && freqs[stack.peek()] > 0) {
                visited[stack.pop()] = false;
            }
            stack.push(c);
            visited[c] = true;
        }
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        return sb.reverse().toString();
    }
}
