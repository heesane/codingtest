// 백준 1021번 문제
// 회전하는 큐

import java.util.*;

public class Main {
    public static void main(String[] args) {
//        입력
//        10 3 // N,M
//        1 2 3 // M개의 수

//        출력
//        0

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] int_list = new int[m];

        for (int i = 0; i < m; i++) {
            int_list[i] = sc.nextInt();
        }

        int count = 0;

        Deque<Integer> q = new LinkedList<>();

        //초기화
        for (int i = 1; i < n+1; i++) {
            q.add(i);
        }

        // m번만큼 반복문 수행
        for(int i =0; i<m;i++){
            int idx = 0;

            for (int j =0; j<q.size();j++){
                if(q.toArray()[j].equals(int_list[i])){
                    idx = j;
                    break;
                }
            }

            int left = idx;
            int right = q.size() - idx;

            if( left < right){
                for(int j =0; j<left;j++){
                    q.offerLast(q.pollFirst());
                    count++;
                }
            }else{
                for(int j =0; j<right;j++){
                    q.offerFirst(q.pollLast());
                    count++;
                }
            }

            q.pollFirst();

        }

        System.out.println(count);

    }
}

