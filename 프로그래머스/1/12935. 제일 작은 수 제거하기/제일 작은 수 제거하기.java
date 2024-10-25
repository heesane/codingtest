import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int minValue = Arrays.stream(arr).min().orElse(Integer.MIN_VALUE);
        return arr.length == 1 
            ? new int[]{-1} 
        : Arrays.stream(arr)
            .filter(e -> e != minValue || (e == minValue && Arrays.stream(arr).filter(n -> n == minValue).count() > 1))
            .toArray();
    }
}