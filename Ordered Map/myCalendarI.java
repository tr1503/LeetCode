// Use treemap's floorKey and ceilingKey to get the lowerbound and upperbound of each input interval
// time is O(nlogn), space is O(n)
class MyCalendar {
    
    TreeMap<Integer, Integer> booked;
    public MyCalendar() {
        booked = new TreeMap<>();
    }
    
    public boolean book(int start, int end) {
        Integer lowerbound = booked.floorKey(start);
        if (lowerbound != null && booked.get(lowerbound) > start)
            return false;
        Integer upperbound = booked.ceilingKey(start);
        if (upperbound != null && upperbound < end)
            return false;
        
        booked.put(start, end);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
