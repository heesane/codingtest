import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        
        ArrayList<Integer> answer = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        for(int t : progresses){
            q.offer(t);
        }
        
        int[] result = progresses;
        int resultIdx = 0;
        
        while(!q.isEmpty()){
            for(int i = progresses.length - q.size();i<progresses.length;i++){
                result[i] += speeds[i];
            }
            
            int q_size = q.size(); 
            int check = 0;

            for(int j =progresses.length - q_size; j<progresses.length;j++){
                if(result[j] >= 100){
                    check++;
                    q.poll();
                    
                    if(q.size() == 0){
                        answer.add(check);
                        return answer;
                    }else{
                        continue;
                    }
                }else if (check>0){
                    answer.add(check);
                    break;
                }else{
                    break;
                }
            }
        }
        
        
        
        return answer;
    }
}