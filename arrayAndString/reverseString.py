class Solution {
    public String reverseString(String s) {
        if (s == null) return null;
        char[] reverse = s.toCharArray();
        for (int i = 0, j = s.length()-1; j > i; i++, j--) {
            char temp = reverse[j];
            reverse[j] = reverse[i];
            reverse[i] = temp;
        }
        return new String(reverse);
    }
}
