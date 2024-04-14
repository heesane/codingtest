import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        List<Integer> answer = new ArrayList<>();
        IntStream.range(0,arr.length)
            .forEach( i -> {
                if(flag[i]){
                    IntStream.range(0,2 * arr[i]).forEach(j ->answer.add(arr[i]));
                }
                else{
                    IntStream.range(0,arr[i]).forEach( j -> answer.remove(answer.size()-1));
                }
            }
        );
        return answer.stream().mapToInt(Integer :: intValue).toArray();
    }
}