class Solution {
    public int candy(int[] ratings) {
        if (ratings.length <= 1)
            return ratings.length;
        int[] candies = new int[ratings.length];
        candies[0] = 1;
        
        //iter from left to right, keep the right one has one more candy if its rating is higher than its left
        //Ohterwise they only get one candy
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i-1])
                candies[i] = candies[i-1] + 1;
            else
                candies[i] = 1;
        }
        
        int sum = candies[candies.length - 1];
        //iter from right to left, keep the higher rating one has one more candy than right one
        for (int i = ratings.length - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i+1]) 
                candies[i] = Math.max(candies[i+1] + 1, candies[i]);
            sum += candies[i];
        }
        return sum;
    }
}
