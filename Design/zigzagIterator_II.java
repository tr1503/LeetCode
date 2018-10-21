public class ZigzagIterator2 {
    /*
    * @param vecs: a list of 1d vectors
    */
    List<Iterator<Integer>> list;
    int count;
    public ZigzagIterator2(List<List<Integer>> vecs) {
        // do intialization if necessary
        count = 0;
        list = new ArrayList<Iterator<Integer>>();
        for (List<Integer> li : vecs) {
            if (!li.isEmpty()) {
                list.add(li.iterator());
            }
        }
    }
 
    /*
     * @return: An integer
     */
    public int next() {
        // write your code here
        int ele = list.get(count).next();
        if (list.get(count).hasNext()) {
            count = (count + 1) % list.size();
        } else {
            list.remove(count);
            if (!list.isEmpty()) {
                count %= list.size();
            }
        }
        return ele;
    }
 
    /*
     * @return: True if has next
     */
    public boolean hasNext() {
        // write your code here
        return list.size() > 0;
    }
}
 
/**
 * Your ZigzagIterator2 object will be instantiated and called as such:
 * ZigzagIterator2 solution = new ZigzagIterator2(vecs);
 * while (solution.hasNext()) result.add(solution.next());
 * Output result
 */
