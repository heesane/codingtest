import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> st = new Stack<>();
        char[] chars = s.toCharArray();
        for(char c : chars){
            if(st.isEmpty()){
                if(c == '('){
                    st.push(c);    
                }else{
                    return false;
                }
            }else if(!st.isEmpty()){
                char temp = st.peek();
                if(temp == '(' && c == ')'){
                    st.pop();
                }else{
                    st.push(c);
                }
            }
        }
        if(st.isEmpty()){
            return true;
        }else return false;
    }
}