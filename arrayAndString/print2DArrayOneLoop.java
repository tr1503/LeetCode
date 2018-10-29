public static void printtwode(int [][]arr){
       for (int r = 0, c = 0; r < arr.length;) {
           if (c < arr[r].length) {
               System.out.println(arr[r][c]);
               ++c;
           } else {
               c = 0;
               ++r;
           }
       }
