class Solution {
    public int calculate(String s) {
        s = s.replaceAll(" ","");
        if (s.length() == 0) 
            return 0;
        Stack<Integer> stack = new Stack<>();
        char sign = '+';
        int res = 0, pre = 0, i = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                pre = pre * 10 + ch - '0';
            }
            if (ch == '(') {
                int j = calClosing(s.substring(i));
                //Use recursion to get the value in the closing paratheses
                pre = calculate(s.substring(i+1,i+j));
                i += j;
            }
            //for new sign, calculate with existing number/sign, then update number/sign
            if (i == s.length() - 1 || !Character.isDigit(ch)) {
                switch(sign) {
                    case '+':
                        stack.push(pre);
                        break;
                    case '-':
                        stack.push(-pre);
                        break;
                    case '*':
                        stack.push(stack.pop() * pre);
                        break;
                    case '/':
                        stack.push(stack.pop() / pre);
                        break;
                }
                pre = 0;
                sign = ch;
            }
            i++;
        }
        while (!stack.isEmpty()) {
            res += stack.pop();
        }
        return res;
    }
    
    //Eliminate all "()" pairs, calculate the result and save in pre
    private int calClosing(String s) {
        int level = 0;
        int i = 0;
        for (; i < s.length(); i++) {
            if (s.charAt(i) == '(')
                level++;
            else if (s.charAt(i) == ')') {
                level--;
                if (level == 0)
                    break;
            }
            else
                continue;
        }
        return i;
    }
}
