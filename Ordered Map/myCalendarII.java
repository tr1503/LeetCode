// Brute force to iterate every time slot and check if it is booked three times
// time is O(n^2), space is O(n)
class MyCalendarTwo {
    List<int[]> calendar;
    List<int[]> overlaps;
    
    public MyCalendarTwo() {
        calendar = new ArrayList<>();   
        overlaps = new ArrayList<>();
    }
    
    public boolean book(int start, int end) {
        for (int[] interval: overlaps) {
            if (interval[0] < end && start < interval[1])
                return false;
        }
        for (int[] interval: calendar) {
            if (interval[0] < end && start < interval[1])
                overlaps.add(new int[]{Math.max(start, interval[0]), Math.min(end, interval[1])});
        }
        calendar.add(new int[]{start, end});
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */
