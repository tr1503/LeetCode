class Solution {
    public String crackSafe(int n, int k) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append("0");
        }
        Set<String> visited = new HashSet<>();
        visited.add(sb.toString());
        dfs(sb,n,k,(int)Math.pow(k,n),visited);
        return sb.toString();
    }
    
    private boolean dfs(StringBuilder sb, int n, int k, int total, Set<String> visited) {
        if (visited.size() == total) {
            return true;
        }
        String curr = sb.substring(sb.length() - n + 1);
        for (char c = '0'; c < '0' + k; c++) {
            if (!visited.contains(curr + c)) {
                sb.append(c);
                visited.add(curr + c);
                if (dfs(sb,n,k,total,visited))
                    return true;
                sb.deleteCharAt(sb.length() - 1);
                visited.remove(curr + c);
            }
        }
        return false;
    }
}
