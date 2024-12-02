class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int row = arr1.length;
        int col = arr1[0].length;
        
        int[][] returnArr = new int[row][col];
        
        for(int i = 0; i < col; i++){
            for(int j = 0; j < row; j++){
                returnArr[j][i] = arr1[j][i] + arr2[j][i];
            }
        }
        return returnArr;
    }
}