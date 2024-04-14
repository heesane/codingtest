class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] b = {"aya", "ye", "woo", "ma"};
        
        for(String bb : babbling){
            
            bb = bb.replace("aya"," ");
            bb = bb.replace("ye"," ");
            bb = bb.replace("woo"," ");
            bb = bb.replace("ma"," ");
            int cnt = 0;
            for(int i =0;i < bb.length();i++){
                if (bb.charAt(i) == ' '){
                    cnt++;
                }
            }
            if(cnt == bb.length()){
                answer++;
            }
            
        }
        return answer;
    }
}