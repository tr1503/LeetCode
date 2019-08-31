// Use tree map in java to search the position after jump
// time is O(nlogn), space is O(n)
class Solution {
    public int oddEvenJumps(int[] A) {
        int n = A.length;
        if (n <= 1)
            return n;
        boolean[] odd = new boolean[n];
        boolean[] even = new boolean[n];
        odd[n-1] = even[n-1] = true;
        
        TreeMap<Integer, Integer> vals = new TreeMap<>();
        vals.put(A[n-1], n-1);
        for (int i = n - 2; i >= 0; i--) {
            int key = A[i];
            if (vals.containsKey(key)) {
                odd[i] = even[vals.get(key)];
                even[i] = odd[vals.get(key)];
            } else {
                Integer lower = vals.lowerKey(key);
                Integer higher = vals.higherKey(key);
                
                if (lower != null)
                    even[i] = odd[vals.get(lower)];
                if (higher != null)
                    odd[i] = even[vals.get(higher)];
            }
            vals.put(key, i);
        }
        
        int res = 0;
        for (boolean b: odd) {
            if (b)
                res++;
        }
        return res;
    }
}
