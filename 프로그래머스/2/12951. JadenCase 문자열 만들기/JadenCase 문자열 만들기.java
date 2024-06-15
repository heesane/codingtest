class Solution {
    public String solution(String s) {
        char[] chars = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        int flag = -1;
        
        for(char c : chars){
            if( Character.isDigit(c) ){
                sb.append(c);
                flag = 1;
            } else{
                if( c == ' '){
                    sb.append(' ');
                    flag = -1;
                    continue;
                }
                
                // 빈 칸이 나온 경우
                if(flag == -1){
                    if( (int)c >= 'a'){ // 소문자가 온 경우 대문자로 변환
                        sb.append((char)((int)c - 32));
                    }else{ // 대문자가 온 경우 그대로 입력
                        sb.append(c);
                    }
                    flag = 1;
                }
                // 빈 칸이 아직 안나온 경우거나 숫자가 나온 경우
                else{
                    if( (int)c >= 'a'){ // 소문자인 경우 그대로 입력
                        sb.append(c);
                    }else{ // 대문자인경우 소문자로 변환
                        sb.append((char)((int) c + 32));
                    }
                
                }
            
            }
        }
        return sb.toString();
    }
}