//Use dp to finish this question, see https://www.jianshu.com/p/bad491f550fa 
class Solution {
    public int getLog(int target) {
        int count = 0;
        int sum = 1;
        while (sum < target) {
            count++;
            sum *= 2;
        }
        return count;
    }
    
    Map<Integer,Integer> visited = new HashMap<>();
    public int racecar(int target) {
        if (visited.containsKey(target))
            return visited.get(target);
        int n = getLog(target + 1);
        int speed = (int)Math.pow(2,n);
        if (speed == target + 1)
            return n;
        int afterward = speed - 1 - target;
        int curr = racecar(afterward) + n + 1;
        for (int i = 0; i < n - 1; i++) {
            int forward = target - (int)Math.pow(2,n-1) + (int)Math.pow(2,i);
            curr = Math.min(curr, racecar(forward) + n + 1 + i);
        }
        visited.put(target,curr);
        return curr;
    }
}
