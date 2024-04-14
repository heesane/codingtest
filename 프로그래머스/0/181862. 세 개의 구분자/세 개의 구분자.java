import java.util.List;
import java.util.ArrayList;
class Solution {
    public String[] solution(String myStr) {
        
        List<String> list = new ArrayList<>();
        
        myStr = myStr.replaceAll("[abc]"," ");

        String temp = "";
        for (int i = 0; i < myStr.length(); i++) {
            if (myStr.charAt(i) == ' ') {
                if (!temp.equals("")) {
                    list.add(temp);
                    temp = "";
                }
            } else {
                temp += myStr.charAt(i);
            }
        }
        
        if (!temp.equals("")) {
            list.add(temp);
        }
        
        if(list.size() == 0){
            list.add("EMPTY");
        }
        return list.toArray(new String[0]);
    }
}