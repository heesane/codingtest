import java.util.*;
class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        List<Integer> arr = new ArrayList();
        char[] c = String.valueOf(n).toCharArray();
        
        for(int i = c.length - 1; i >=0; i--){
            arr.add(c[i]-'0');
        }
        
        return arr.stream().mapToInt(i -> i).toArray();
    }
}