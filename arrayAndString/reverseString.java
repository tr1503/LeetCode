class Solution {
    public String reverseString(String s) {
        // if (s == null)
        //     return null;
        // char[] reverse = s.toCharArray();
        // for (int i = 0, j = reverse.length - 1; j > i; i++, j--) {
        //     char temp = reverse[i];
        //     reverse[i] = reverse[j];
        //     reverse[j] = temp;
        // }
        // return new String(reverse);
        int length = s.length();
        if (length <= 1)
            return s;
        String left = s.substring(0, length / 2);
        String right = s.substring(length / 2, length);
        return reverseString(right) + reverseString(left);
    }
}
