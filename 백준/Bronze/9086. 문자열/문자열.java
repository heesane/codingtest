// 9086 - 문자열 - 브론즈 5

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int repeat = Integer.parseInt(br.readLine());

        for(int i = 0; i < repeat; i++){
            String temp = br.readLine();
            System.out.println(temp.charAt(0)+""+temp.charAt(temp.length()-1));
        }
    }
}