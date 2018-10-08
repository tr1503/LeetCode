class Solution {
    public boolean isNumber(String s) {
        s = s.trim();
        boolean number = false;
        boolean point = false;
        boolean e = false;
        boolean numAfterE = true;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                number = true;
                numAfterE = true;
            }
            else if (s.charAt(i) == '.') {
                if (point || e)
                    return false;
                point = true;
            }
            else if (s.charAt(i) == 'e') {
                if (e || !number) 
                    return false;
                e = true;
                //the string must have numbers after e can be a valid number
                numAfterE = false;
            }
            else if (s.charAt(i) == '+' || s.charAt(i) == '-') {
                if (i != 0 && s.charAt(i-1) != 'e')
                    return false;
            }
            else {
                return false;
            }
        }
        return number && numAfterE;
    }
}
