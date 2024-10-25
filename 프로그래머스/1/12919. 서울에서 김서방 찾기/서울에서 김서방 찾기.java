import java.util.stream.IntStream;

class Solution {
    public String solution(String[] seoul) {
        int idx = IntStream.range(0, seoul.length)
                             .filter(i -> "Kim".equals(seoul[i]))
                             .findFirst()
                             .orElse(-1);
        return "김서방은 "+idx+"에 있다";
    }
}