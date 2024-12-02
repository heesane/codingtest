class Solution {
    public boolean solution(String s) {
        
        if(s.length() == 4 || s.length() ==6){
            char[] sChar = s.toCharArray();
        
            int count = 0;

            for(char c : sChar){
                if(Character.isDigit(c)){
                    count++;
                }
            }
            if(count == s.length() ){
                return true;
            }else{
                return false;
            }
        }
        return false;
    }
}