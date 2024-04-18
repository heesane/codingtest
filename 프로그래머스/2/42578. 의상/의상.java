import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer =1;
        HashMap<String,Integer> hm = new HashMap<>();
        for(String[] clothe: clothes){
            
            String category = clothe[clothe.length-1]; // 카테고리
            String clothe_name = clothe[0]; // 옷 이름
            
            if(hm.containsKey(category)){
                hm.put(category,hm.get(category) + 1);
            }
            else{
                hm.put(category,2);
            }
        }
        
        for(Integer t : hm.values()){
            answer *= t;
        }
        
        
        
        return answer - 1;
    }
}