import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Main{
    public static void main(String[] args)
            throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> nums = new ArrayList<>();

        for (int i = 0; i <N ; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }
        // [19,10...]
        int[] count = new int[20];
        for(Integer num: nums){
            int idx = 0;
            while(num > 0){
                count[idx++] += num % 2;
                num /= 2;
            }
        }
        long sum = 0L;
        for (int i = 19; i >= 0; i--) {
            sum += (long)count[i] * (N - count[i]);
            sum <<= 1;
        }
        sum >>= 1;
        System.out.println(sum);

    }
}