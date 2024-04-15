import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        Stack<Integer> st = new Stack<>();
        
        for(int num : arr){
            if(st.size() == 0){
                st.push(num);
                continue;
            }
            if(num == st.peek()){
                continue;
            }
            else{
                st.push(num);
            } 
        }
        int[] ret_int = new int[st.size()];
        int idx = 0;
        for(int s:st){
            ret_int[idx++] = s;
        }
        return ret_int;
    }
}