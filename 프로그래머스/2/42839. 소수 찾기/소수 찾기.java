// 백트래킹
import java.util.*;
class Solution {
    public int solution(String numbers) {
        int answer = 0;
        
        HashSet<Integer> hs = new HashSet<>();
        boolean[] visited = new boolean[7];
        dfs(numbers,"",0,visited,hs);
        
        for(int n : hs){
            if(isPrime(n)) answer++;
        }
        
        return answer;
        
    }
    
    public void dfs(String numbers, String s, int depth,boolean[] visited, HashSet<Integer> hash){
        if(depth > numbers.length()) return;
            
        for(int i = 0; i<numbers.length();i++){
            if(!visited[i]){ // 방문하지 않은 경우
                visited[i] = true;
                String temp = s + numbers.charAt(i);
                hash.add(Integer.parseInt(temp));
                dfs(numbers,temp,depth+1,visited,hash);
                visited[i] = false;
            }
        }
    }
    
    public boolean isPrime(int number){
        if (number == 0 || number == 1) return false;
        
        for(int i = 2; i <= Math.sqrt(number); i++){
            if(number % i == 0) return false;
        }
        return true;
    }
}