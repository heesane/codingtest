import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> int_list = new ArrayList<>();

        for(int i =0; i< arr.length; i++){
            if(arr[i] == 2){
                int_list.add(i);
            }
        }
        
        if(int_list.size() == 0){
            int_list.add(-1);
        } else if(int_list.size() == 1){
            int_list.clear();
            int_list.add(2);
        } else{
            int start_idx = int_list.get(0);
            int end_idx = int_list.get(int_list.size()-1);
            int_list.clear();
            for(int i = start_idx; i < end_idx + 1;i++){
                int_list.add(arr[i]);
            }
            
        }
         
                
        return int_list.stream().mapToInt(Integer::intValue).toArray();
    }
}