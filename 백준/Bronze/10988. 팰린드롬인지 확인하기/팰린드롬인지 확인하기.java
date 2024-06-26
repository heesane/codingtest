// 10988 - 팰린드롬인지 확인하기 - 7 - 브론즈 3

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
    private static int palindrome(String string){
        int start = 0;
        int end = string.length() - 1;
        while(start < end){
            if(string.charAt(start) != string.charAt(end)){
                return 0;
            }
            start++;
            end--;
        }
        return 1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(palindrome(br.readLine()));
    }
}