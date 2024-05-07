import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        char[] c = s.toCharArray();
        HashMap<Character,Integer> map = new HashMap<>();
        
        for(char t : c){
            map.put(t,map.getOrDefault(t,0) + 1);
        }
        
        for(Map.Entry<Character,Integer> temp : map.entrySet()){
            if(temp.getValue() ==1){
                answer+= temp.getKey();
            }
        }
        
        char[] a = answer.toCharArray();
        Arrays.sort(a);
        answer = new String(a);
        return answer;
    }
}