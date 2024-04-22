import java.util.*;
class Solution {
    public int solution(String s) {
        String answer_str = "";
        int answer = 0;
        HashMap<String,Integer> dictionary = new HashMap<>();
        dictionary.put("zero",0);
        dictionary.put("one",1);
        dictionary.put("two",2);
        dictionary.put("three",3);
        dictionary.put("four",4);
        dictionary.put("five",5);
        dictionary.put("six",6);
        dictionary.put("seven",7);
        dictionary.put("eight",8);
        dictionary.put("nine",9);
        String temp = "";
        for(char c : s.toCharArray()){
            if(Character.isDigit(c)){
               answer_str += String.valueOf(c);
            }
            else{
                temp += c;
                
                if(dictionary.containsKey(temp)){
                    answer_str += String.valueOf(dictionary.get(temp));
                    temp = "";
                }
            }
        }
        
        return Integer.parseInt(answer_str);
    }
}