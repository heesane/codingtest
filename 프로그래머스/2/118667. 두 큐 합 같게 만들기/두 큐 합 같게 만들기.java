import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        int N = queue1.length;
        long sum1 = 0;
        long sum2 = 0;

        for (int i = 0; i < N; i++) {
            sum1 += queue1[i];
            sum2 += queue2[i];
        }

        if ((sum1 + sum2) % 2 == 1) {
            return -1;
        }

        long total = (sum1 + sum2) / 2;
        int[] arr = new int[2 * N];

        for (int i = 0; i < N; i++) {
            arr[i] = queue1[i];
        }

        for (int i = 0; i < N; i++) {
            arr[i + N] = queue2[i];
        }
       
        int point1 = 0;
        int point2 = N;
        
        long sum = sum1;

        while (point1 < point2) {
            if (sum == total) {
                break;
            }
            
            if (sum < total && point2 == 2 * N - 1) {
                break;
            }

            if (sum > total) {
                sum -= arr[point1];
                point1++;
            }
            else if (sum < total) {
                sum += arr[point2];
                point2++;
            } 

            answer++;
        }

        if (sum != total) {
            answer = -1;
        }

        return answer;
    }
}