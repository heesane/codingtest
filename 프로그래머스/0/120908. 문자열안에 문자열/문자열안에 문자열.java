class Solution {
    public int solution(String str1, String str2) {
        int answer = 2;
        for(int i = 0;i<str1.length() - str2.length()+1;i++){
            String sub = str1.substring(i,i+str2.length());
            if(sub.equals(str2)) return 1;
        }
        return answer;
    }
}