import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public String solution(String s) {
        
        return s.chars()
                  .boxed()
                  .sorted((a, b) -> b - a)
                  .map(c -> String.valueOf((char) c.intValue()))
                  .collect(Collectors.joining());
    }
}