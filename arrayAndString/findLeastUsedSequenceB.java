public int findLeastUsedB(String A, String B) {
        Map<Character, List<Integer>> map = new HashMap<>();
        for(int i = 0; i < B.length(); i++) {
            List<Integer> list = map.get(B.charAt(i));
            if(list == null) {
                list = new ArrayList<>();
                map.put(B.charAt(i), list);
            }
            list.add(i);
        }
         
        int index = 0;
        int res = 1;
        for(int i = 0; i < A.length(); i++) {
            char c = A.charAt(i);
            List<Integer> list = map.get(c);
            if(list == null) {
                return -1; // which means there is no way to build the String A
            }
            int id = Collections.binarySearch(list, index);
            if(id < 0) {
                id = -id - 1;
            }
            if(id == list.size()) {
                res++;
                index = list.get(0) + 1;
            } else {
                index = list.get(id) + 1;
            }
        }
        return res;
    }
