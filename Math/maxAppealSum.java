// "static void main" must be defined in a public class.
//https://leetcode.com/discuss/interview-question/355698/amazon-oa-2019-find-pair-with-max-appeal-sum/323219
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        //int[] a = new int[]{1, 3, -1};
        //int[] a = new int[]{1, 2, 6, 7, 4, 1, 5};
        int[] a = new int[]{3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1};
        int[] pair = maxAppealVal(a);
        System.out.println(pair[0]+ " "+pair[1]);
    }
    
    
    //O(n) time complexity
    //O(1) space
    private static int[] maxAppealVal(int[] arr) {
        if (arr == null || arr.length == 0)
            return new int[]{-1, -1};
        int max1 = Integer.MIN_VALUE;
        int max2 = Integer.MIN_VALUE;
        int m1 = -1;
        int m2 = -1;
        for (int i = 0; i < arr.length; i++) {
            int curr1 = arr[i] + i;
            int curr2 = arr[i] - i;
            
            if (curr1 > max1) {
                max1 = curr1;
                m1 = i;
            }
            
            if (curr2 > max2) {
                max2 = curr2;
                m2 = i;
            }
        }
        return new int[]{m1, m2};
    }
}
