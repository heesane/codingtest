// 11718 - 그대로 출력하기 - 브론즈 3

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S;
        while((S = br.readLine()) != null) {
            System.out.println(S);
        }
    }
}