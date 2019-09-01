class RangeModule {
    TreeMap<Integer, Integer> intervals;
    
    public RangeModule() {
        intervals = new TreeMap<>();
    }
    
    // time is O(nlogn)
    public void addRange(int left, int right) {
        Integer start = intervals.floorKey(left);
        Integer end = intervals.floorKey(right);
        if (start != null && intervals.get(start) >= left) {
            left = start;
        }
        if (end != null && intervals.get(end) > right) {
            right = intervals.get(end);
        }
        intervals.put(left, right);
        intervals.subMap(left, false, right, true).clear();
    }
    
    // time is O(logn)
    public boolean queryRange(int left, int right) {
        Integer start = intervals.floorKey(left);
        if (start == null)
            return false;
        return intervals.get(start) >= right;
    }
    
    // time is O(nlogn)
    public void removeRange(int left, int right) {
        Integer start = intervals.floorKey(left);
        Integer end = intervals.floorKey(right);
        
        if (end != null && intervals.get(end) > right) {
            intervals.put(right, intervals.get(end));
        }
        if (start != null && intervals.get(start) > left) {
            intervals.put(start, left);
        }
        intervals.subMap(left, true, right, false).clear();
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * boolean param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */
