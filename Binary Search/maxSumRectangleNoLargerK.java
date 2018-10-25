// For each set of column [i..j), do it like count of range sum.
// Time is O(n^2 * mlongm), n is rows, m is cols
class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length;
        int n = matrix[0].length;
        int ans = Integer.MIN_VALUE;
        long[] sum = new long[m+1]; // stores sum of rect[0..p][i..j]
        for (int i = 0; i < n; i++) {
            long[] sumInRow = new long[m];
            for (int j = i; j < n; j++) { // for each rect[*][i..j]
                for (int p = 0; p < m; p++) {
                    // calculate each sub-rectangle in matrix
                    sumInRow[p] += matrix[p][j];
                    sum[p+1] = sum[p] + sumInRow[p];
                }
                // use the merge sort (binary search) to get the value smaller than k
                ans = Math.max(ans, mergeSort(sum, 0, m+1, k));
                if (ans == k)
                    return k;
            }
        }
        return ans;
    }
    
    private int mergeSort(long[] sum, int start, int end, int k) {
        if (end == start + 1) // need at least two element to process
            return Integer.MIN_VALUE;
        int mid = start + (end - start) / 2;
        int count = 0;
        int ans = mergeSort(sum, start, mid, k);
        if (ans == k)
            return k;
        ans = Math.max(ans, mergeSort(sum, mid, end, k));
        if (ans == k)
            return k;
        long[] cache = new long[end - start];
        for (int i = start, j = mid, p = mid; i < mid; i++) {
            while (j < end && sum[j] - sum[i] <= k) {
                j++;
            }
            if (j - 1 >= mid) {
                ans = Math.max(ans, (int)(sum[j-1] - sum[i]));
                if (ans == k) 
                    return k;
            }
            while (p < end && sum[p] < sum[i]) {
                cache[count++] = sum[p++];
            }
            cache[count++] = sum[i];
        }
        System.arraycopy(cache, 0, sum, start, count);
        return ans;
    }
}
