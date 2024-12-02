

class Solution {
    
    public int getDivided(int number){
    int ans = 0;
    for(int i = 1; i < number + 1; i++){
        if (number % i == 0){
            ans++;
        }
    }
    return ans;
}
    
    public int solution(int left, int right) {
        int answer = 0;
        
        for(int i = left; i < right + 1; i++){
            if(getDivided(i) % 2 == 0){
                answer += i;
            }else{
                answer -= i;
            }
        }
        
        return answer;
    }
} 