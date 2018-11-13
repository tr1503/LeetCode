/*  Use Greedy Algorithm to set 10 buckets which represent 0-9, and set their values to their last appearing index.
    Pass the number, if we find one bucket's value is larger than current index's value means there is a large 
    number is behind the small number, so swap it and return the result
*/
class Solution {
    public int maximumSwap(int num) {
        char[] A = Integer.toString(num).toCharArray();
        int[] last = new int[10];
        for (int i = 0; i < A.length; i++) {
            last[A[i] - '0'] = i;
        }
        
        for (int i = 0; i < A.length; i++) {
            for (int d = 9; d > A[i] - '0'; d--) {
                if (last[d] > i) {
                    char temp = A[i];
                    A[i] = A[last[d]];
                    A[last[d]] = temp;
                    return Integer.valueOf(new String(A));
                }
            }
        }
        return num;
    }
}
