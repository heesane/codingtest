import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);

        int N = sc.nextInt();

        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            arr.add( sc.nextInt());
        }
        int max = Collections.max(arr);
        int min = Collections.min(arr);
        System.out.println(min+" "+max);

    }
}