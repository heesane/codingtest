import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        if(triangle.length == 1 ) return triangle[0][0];
        for(int i = 1; i < triangle.length;i++){
            triangle[i][0] += triangle[i-1][0];
            triangle[i][i] += triangle[i-1][i-1];
            
            for(int j = 1; j < i; j++){
                triangle[i][j] = Math.max(triangle[i-1][j-1] + triangle[i][j],triangle[i-1][j] + triangle[i][j]);
            }
        }
        int[] res = triangle[triangle.length - 1];
        
        
        return Arrays.stream(res).max().getAsInt();
    }
}