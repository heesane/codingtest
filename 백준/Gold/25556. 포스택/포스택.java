import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        //비교를 위한 가장 작은 수를 각 스택에 삽입한다.
        Stack<Integer>[] stacks = new Stack[4];
        for(int i=0; i<4; i++) {
            stacks[i] = new Stack<>();
            stacks[i].push(0);
        }

        //스택의 peek보다 큰 수라면 삽입하기
        for(int i=0; i<n; i++) {
            boolean flag = false;
            for(int j=0; j<4; j++) {
                if(stacks[j].peek() < arr[i]) {
                    stacks[j].push(arr[i]);
                    flag = true;
                    break;
                }
            }

            //모든 스택에 삽입하지 못 했다면
            if(!flag) {
                System.out.println("NO");
                return;
            }
        }

        //순열 청소가 완료되면
        System.out.println("YES");

    }
}