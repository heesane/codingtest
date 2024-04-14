class Solution {
    public int solution(int n) {
        int answer = 0;
        int t = 1;
        while(true){
            if (n % t == 1) return t;
            t++;
        }
    }
}