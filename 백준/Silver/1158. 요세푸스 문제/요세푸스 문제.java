// 백준 1158번 요세푸스 문제

import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        LinkedList<Integer> ll = new LinkedList<>();

        for (int i = 1; i < N+1; i++) {
            ll.add(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        int idx = 0; // 시작점

        while (!ll.isEmpty()) {
            idx = (idx + K - 1) % ll.size();
            sb.append(ll.remove(idx));
            if (!ll.isEmpty()) {
                sb.append(", ");
            }
        }
        sb.append(">");

        System.out.println(sb);
    }
}