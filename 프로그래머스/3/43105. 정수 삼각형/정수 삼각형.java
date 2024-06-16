class Solution {
    public int solution(int[][] triangle) {
        if(triangle.length == 1 ) return triangle[0][0];
        // 어느 방향으로 가든 갈 수 있는 idx는 다음 레벨의 현재 idx, idx + 1
        int answer = 0;
        int[][] dp = new int[triangle.length+1][triangle.length];
        
        for(int i = 1; i < triangle.length+1; i++){ // 층 증가
            for(int j = 0; j < triangle[i-1].length; j++){ // 해당 층에 있는 모든 노드 검사
                for(int k = j-1; k < j+1; k++){ // 다음 층 검사
                    if(k < 0) continue;
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][k] + triangle[i-1][j]);
                    answer = Math.max(dp[i][j], answer);
                }
            }
        }
        
        return answer;
    }
}