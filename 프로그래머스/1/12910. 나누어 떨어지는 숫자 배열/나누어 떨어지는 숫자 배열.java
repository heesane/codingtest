import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> arr_list = new ArrayList<>();
        
        for(int n : arr){
            if(n % divisor == 0){
                arr_list.add(n);
            }
        }
        
        if(arr_list.isEmpty()) {
            int[] answer = {-1};
            return answer;
        }
        
        int[] answer = new int[arr_list.size()];
        for (int i = 0; i< answer.length;i++){
            answer[i] = arr_list.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}