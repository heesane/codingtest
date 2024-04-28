import java.util.Arrays;
class Solution {
    public int solution(int[][] routes) {
        int answer = 1;
        Arrays.sort(routes,(a,b) -> a[1] - b[1]);
        // System.out.println(Arrays.deepToString(routes));
        int line = routes[0][1];
        for(int i = 0; i < routes.length;i++){
            if(line < routes[i][0]){
                line = routes[i][1];
                answer ++;
            }
        }
        return answer;
    }
}