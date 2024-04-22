import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Main{
    public static void main(String[] args)
            throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        ArrayList<Integer> list = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            list.add(Integer.parseInt(st.nextToken()));
        }

        int target = Integer.parseInt(br.readLine());
        int count = 0;

        for (int i = 0; i < N ; i++) {
            if (list.get(i) == target) {
                count++;
            }
        }
        System.out.println(count);

    }
}