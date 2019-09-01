// Because the matrix is sparse matrix, we can skip some extra multiplation for 0
// we can add the contribution of each number to the product matrix
class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        int ARow = A.length;
        int AColumn = A[0].length;
        int BRow = B.length;
        int BColumn = B[0].length;
        
        int[][] product = new int[ARow][BColumn];
        for (int i = 0; i < ARow; i++) {
            for (int j = 0; j < AColumn; j++) {
                if (A[i][j] == 0)
                    continue;
                for (int k = 0; k < BColumn; k++) {
                    product[i][k] += A[i][j] * B[j][k];
                }
            }
        }
        return product;
    }
}
