import java.util.HashMap;
class Solution {
    public static int solution(String[] strArr) {
        int answer = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        int max = 0;
        for(int i = 0; i < strArr.length;i++){
            if(map.get(strArr[i].length()) == null){
                map.put(strArr[i].length(), 1);
            }else{
            map.put(strArr[i].length(),map.get(strArr[i].length())+1);
        
            }
        }
        for (Integer k : map.keySet()){
            if(map.get(k) > max){
                max = map.get(k);
            }
        }
        return max;
    }
}