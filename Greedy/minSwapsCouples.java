// Use xor operator and greedy algorithm to solve this question
// Any number can get their pair by xor 1
class Solution {
    public int minSwapsCouples(int[] row) {
        int res = 0;
        int n = row.length;
        for (int i = 0; i < n; i += 2) {
            if (row[i+1] == (row[i] ^ 1))
                continue;
            res++;
            for (int j = i + 1; j < n; j++) {
                if (row[j] == (row[i] ^ 1)) {
                    row[j] = row[i+1];
                    row[i+1] = row[i] ^ 1;
                    break;
                }
            }
        }
        return res;
    }
}
