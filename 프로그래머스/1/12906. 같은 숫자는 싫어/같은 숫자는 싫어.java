import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        Deque<Integer> dq = new ArrayDeque<>();
        
        for(int num : arr){
            if(dq.size() == 0){
                dq.offerLast(num);
                continue;
            }
            if(num == dq.peekLast()){
                continue;
            }
            else{
                dq.offerLast(num);
            } 
        }
        int[] ret_int = new int[dq.size()];
        int idx = 0;
        for(int d:dq){
            ret_int[idx++] = d;
        }
        return ret_int;
    }
}