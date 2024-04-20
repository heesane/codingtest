// 백준 24174번 힙 정렬

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// max heap sort = 오름차순
// min heap sort = 내림차순

class Main{
    public static int cnt = 0, target = 0;
    public static boolean flag = false;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        target = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N ; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        heapSort(arr);
        if(!flag){
            System.out.println(-1);
        }
    }

    // swap
    // 해당 문제에서는 cnt에 맞춰서 StringBuilder로 출력
    public static void swap(int[] arr ,int i, int j){
        cnt++;
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

        if(target == cnt){
            StringBuilder sb = new StringBuilder();
            for (int k = 0; k < arr.length; k++) {
                sb.append(arr[k]).append(" ");
            }
            System.out.println(sb);
            flag= true;
        }
    }

    // min heap 만드는 과정
    public static void min_heapify(int[] arr, int parentIdx, int lastIdx){
        int left= parentIdx * 2 + 1;
        int right = parentIdx * 2 + 2;
        int largestIdx = parentIdx;

        if(left <= lastIdx && arr[left] < arr[largestIdx]){
            largestIdx = left;
        }
        if(right <= lastIdx && arr[right] < arr[largestIdx]){
            largestIdx= right;
        }

        if(parentIdx != largestIdx){
            swap(arr,parentIdx,largestIdx);
            min_heapify(arr,largestIdx,lastIdx);
        }

    }
    // max heap 만드는 과정
    public static void max_heapify(int[] arr, int parentIdx, int lastIdx){
        int left= parentIdx * 2 + 1;
        int right = parentIdx * 2 + 2;
        int largestIdx = parentIdx;

        if(left <= lastIdx && arr[left] > arr[largestIdx]){
            largestIdx = left;
        }
        if(right <= lastIdx && arr[right] > arr[largestIdx]){
            largestIdx = right;
        }

        if(parentIdx != largestIdx){
            swap(arr,parentIdx,largestIdx);
            max_heapify(arr,largestIdx,lastIdx);
        }
    }

    // 부모노드 찾기
    public static int getParent(int idx){
        return (idx - 1) / 2;
    }
    public static void heapSort(int[] arr){
        int size = arr.length;

        if(size < 2) return;

        // 부모노드 찾기
        int parentIdx = getParent(size - 1);

        // heap 만드는 과정
        for (int i = parentIdx; i >= 0 ; i--) {
            // max_heapify(arr,i,size - 1);
            // 부모노드부터, 0번 인덱스까지
            // 자식 노드의 -1 level부터 0 level까지 탐색하면서, 최대 및 최소 힙 생성
            min_heapify(arr,i,size-1);

        }

        // 정렬하는 과정
        for (int i = size - 1; i > 0  ; i--) {
            // 맨 앞 노드와 뒤 노드 위치 전환
            swap(arr,0,i);
            // max_heapify(arr,0,i-1);
            min_heapify(arr,0,i-1);
        }
    }

}