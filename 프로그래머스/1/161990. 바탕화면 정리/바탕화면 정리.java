import java.util.*;
class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {51,51,-1,-1};
        int row = 0; //행
        
        for(String s : wallpaper){
            int col = 0;
            char[] chars = s.toCharArray();
            for(char c : chars){
                if(c == '#'){
                    answer[0] = Math.min(answer[0],row);
                    answer[1] = Math.min(answer[1],col);
                    answer[2] = Math.max(answer[2],row+1);
                    answer[3] = Math.max(answer[3],col+1);
                }
                col++;
            }
            row++;
        }
        
        return answer;
    }
}