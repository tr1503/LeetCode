class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, (s1, s2) -> {
            int index1 = s1.indexOf(' ');
            int index2 = s2.indexOf(' ');
            String l1 = s1.substring(index1 + 1);
            String l2 = s2.substring(index2 + 1);
            
            if (l1.charAt(0) <= '9') {
                if (l2.charAt(0) <= '9') 
                    return 0;
                else
                    return 1;
            }
            else {
                if (l2.charAt(0) <= '9')
                    return -1;
                else {
                    int cmpContent = l1.compareTo(l2);
                    if (cmpContent != 0)
                        return cmpContent;
                    return s1.substring(0, index1).compareTo(s2.substring(0, index2));
                }
            }
        });
        return logs;
    }
}
