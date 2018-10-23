class Solution {
    public int nextGreaterElement(int n) {
        char[] s = ("" + n).toCharArray();
        int i = s.length - 2;
        while (i >= 0 && s[i + 1] <= s[i]) {
            i--;
        }
        if (i < 0)
            return -1;
        int j = s.length - 1;
        while (j >= 0 && s[j] <= s[i]) {
            j--;
        }
        swap(s,i,j);
        reverse(s, i+1);
        try {
            return Integer.parseInt(new String(s));
        } catch (Exception e) {
            return -1;
        }
    }
    
    private void reverse(char[] s, int start) {
        int i = start;
        int j = s.length - 1;
        while (i < j) {
            swap(s, i, j);
            i++;
            j--;
        }
    }
    
    private void swap(char[] s, int i, int j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}
