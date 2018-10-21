class Solution {
    public double minmaxGasDist(int[] stations, int K) {
        double left = 0;
        double right = 1e8;
        while (right - left > 1e-6) {
            double mid = left + (right - left) / 2;
            int count = 0;
            for (int i = 0; i < stations.length - 1; i++) {
                count += (stations[i+1] - stations[i]) / mid;
            }
            if (count <= K)
                right = mid;
            else
                left = mid;
        }
        return left;
    }
}
