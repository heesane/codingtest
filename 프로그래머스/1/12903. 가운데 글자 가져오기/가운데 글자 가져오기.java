class Solution {
    public String solution(String s) {
        String answer = "";
        
        int sLen = s.length();
        
        // 짝수
        if(sLen % 2 == 0){
            return s.substring(sLen / 2 - 1 ,sLen / 2+1);
        }
        // 홀수
        else{
            return Character.toString(s.charAt(sLen / 2));
        }
    }
}