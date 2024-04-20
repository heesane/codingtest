// 백준 24174번 힙 정렬

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main{
    public static int cnt = 0, target = 0;
    public static boolean isOut = false;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input  = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = input[0]; // 배열 A의 크기
        target = input[1]; // 교환 횟수

        int[] arr = new int[n+1];
        arr[0] = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) arr[i] = Integer.parseInt(st.nextToken());

        heap_sort(arr);
        if(!isOut){
            System.out.print(-1);
        }
    }

    public static void swap(int[] arr,int i, int j){
        cnt++;
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

        if(cnt == target){
            StringBuilder sb= new StringBuilder();
            for (int k = 1; k < arr.length; k++) {
                sb.append(arr[k]).append(" ");
            }
            System.out.print(sb);
            isOut = true;
        }
    }

    public static void heap_sort(int[] arr){
        build_min_heap(arr,arr.length - 1);
        for (int i = arr.length - 1; i > 1 ; i--) {
            swap(arr,1,i);
            heapify(arr,1,i-1);
        }
    }
    public static void build_min_heap(int[] arr, int n){
        for (int i = n/2; i >= 1 && !isOut; i--) {
            heapify(arr,i,n);
        }
    }
    public static void heapify(int[] arr, int k, int n){
        int left = 2* k;
        int right = 2*k+1;
        int smaller = -1;;

        if(right <= n){
            smaller = arr[left] < arr[right] ? left : right;
        }
        else if (left <= n){
            smaller = left;
        }
        else{
            return;
        }

        if(arr[smaller] < arr[k]){
            swap(arr,k,smaller);
            heapify(arr,smaller,n);
        }
    }

}