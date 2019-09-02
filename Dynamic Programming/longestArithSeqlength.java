// Use dynamic programming to compare a[i]-a[j] to get the status and iterate
// Use list and hashmap to create a table and memorize the length
// time is O(n^2), space is O(n^2)
class Solution {
    public int longestArithSeqLength(int[] A) {
        List<Map<Integer, Integer>> table = new ArrayList<>();
        table.add(new HashMap<>());
        
        int max = 0;
        for (int i = 1; i < A.length; i++) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j < i; j++) {
                int diff = A[i] - A[j];
                Map<Integer, Integer> map = table.get(j);
                int currMax = map.getOrDefault(diff, 1) + 1;
                curr.put(diff, currMax);
                max = Math.max(max, currMax);
            }
            table.add(curr);
        }
        return max;
    }
}
