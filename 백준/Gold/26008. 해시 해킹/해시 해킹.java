// 백준 26008번 해시 해킹 골드3

import java.util.*;

class Main{
    public static void main(String[] args) {

        int DIVIED = 1000000007;
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int A = sc.nextInt();

        int H = sc.nextInt();
        long answer = 1L;
        for(int i = 0 ; i <N-1;i++ ){
            answer = (answer * M) % DIVIED;
        }
        System.out.println(answer);
        
    }
}