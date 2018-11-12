// Use union find finish this question, get all connected component of similar words,
// get the count of all connected components.
class Solution {
    private boolean isSimilar(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
                if (count > 2) 
                    return false;
            }
        }
        // Use count == 0 to consider the situation that all words are same
        return count == 2 || count == 0;
    }
    
    private int find(int[] f, int id) {
        while (id != f[id]) {
            f[id] = f[f[id]];
            id = f[id];
        }
        return id;
    }
    
    public int numSimilarGroups(String[] A) {
        Set<String> set = new HashSet<>(Arrays.asList(A));
        int n = set.size();
        int res = n;
        int index = 0;
        String[] B = new String[n];
        for (String s : set) {
            B[index++] = s;
        }
        int[] f = new int[n];
        for (int i = 0; i < n; i++) {
            f[i] = i;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = find(f, i);
                int b = find(f, j);
                if (a == b || !isSimilar(B[i],B[j]))
                    continue;
                f[a] = b;
                res--;
            }
        }
        return res;
    }
}
