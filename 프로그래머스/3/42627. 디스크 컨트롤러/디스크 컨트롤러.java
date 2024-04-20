import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int cnt = 0;
        int job_idx = 0;
        int end = 0;
        
        Arrays.sort(jobs,(o1,o2) -> o1[0] - o2[0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1,o2) -> o1[1] - o2[1]);
        
        int time = 0;
        
        while(cnt < jobs.length){
            while(job_idx < jobs.length && jobs[job_idx][0] <= end){
                pq.add(jobs[job_idx]);
                job_idx++;
            }
            if(pq.isEmpty()){
                end = jobs[job_idx][0];
            }
            else{
                int[] temp = pq.poll();
                answer += temp[1] + end - temp[0];
                end += temp[1];
                cnt++;
            }
        }
        return (int)Math.floor(answer / jobs.length);
    }
}