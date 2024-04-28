import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 도시 수
        int[] cities = new int[N-1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N-1; i++) {
            cities[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int[] oils = new int[N];
        for (int i = 0; i < N; i++) {
            oils[i] = Integer.parseInt(st.nextToken());
        }
        int total = 0;
        int oil = oils[0];
        for (int i = 0; i < N-1; i++) {
            if(oil > oils[i]) oil = oils[i];
            total += oil*cities[i];
        }


        System.out.println(total);

    }
}