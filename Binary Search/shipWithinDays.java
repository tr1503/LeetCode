// Same as the question Split Array Largest Sum
// time is O(nlogn), space is O(1)
class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int left = 0;
        int right = 0;
        for (int weight : weights) {
            left = Math.max(left, weight);
            right += weight;
        }
        right++;
        
        while (left < right) {
            int mid = left + (right - left >> 1);
            int day = getDays(weights, mid);
            if (day <= D)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
    
    private int getDays(int[] weights, int limit) {
        int day = 1;
        int sum = 0;
        for (int weight : weights) {
            if (sum + weight > limit) {
                sum = weight;
                day++;
            }
            else
                sum += weight;
        }
        return day;
    }
}
