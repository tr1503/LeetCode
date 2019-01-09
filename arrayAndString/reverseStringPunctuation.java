    public static String reverse(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
 
        List<String> list = new ArrayList<>(); // list of words
        StringBuilder sb = new StringBuilder(); // buffer
        int i = 0;
        while (i < s.length()) {
            if (!Character.isLetter(s.charAt(i))) {
                sb.append(s.charAt(i));
                i++;
                continue;
            }
 
            int j = i + 1;
            while (j <= s.length() && Character.isLetter(s.charAt(j))) {
                j++;
            }
 
            list.add(s.substring(i, j));
            sb.append("a");
 
            i = j;
        }
 
        String temp = sb.toString();
        StringBuilder res = new StringBuilder();
        int currWordPosition = list.size() - 1;
 
        for (int k = 0; k < temp.length(); k++) {
            if (temp.charAt(k) == 'a') {
                res.append(list.get(currWordPosition--));
            } else {
                res.append(temp.charAt(k));
            }
        }
 
        return res.toString();
    }
}
