// 10809 - 알파벳 찾기 - 브론즈 2

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S = br.readLine();

        int[] arr = new int[26];

        Arrays.fill(arr, -1);

        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if(arr[c -'a'] == -1){
                arr[c - 'a'] = i;
            }
        }

        Arrays.stream(arr).forEach(i -> //join with space 맨 뒤에는 빈칸이 없어야함
            System.out.print(i + " ")
        );
    }
}