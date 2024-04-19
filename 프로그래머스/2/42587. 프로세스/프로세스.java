import java.util.*;

class Solution {
        public int solution(int[] priorities, int location) {
            int answer = 0;
            LinkedList<Integer> ll = new LinkedList<>();
            
            // LinkedLis로 priorities 넣기
            for(int n: priorities){
                ll.add(n);
            }
            
            // ll 순회
            while(!ll.isEmpty()){
                // max 값 찾기
                int max = 0;
                for(Integer n : ll){
                    if (n > max){
                        max = n;
                    }
                }
                
                // 0번 인덱스 조회
                // 0번 인덱스 값이 max인경우,
                if(ll.peek() == max){
                    ll.poll();
                    answer++;
                    // location이 0인 경우, 종료
                    // 아닌 경우, poll로 인한 재배열
                    // location--
                    if(location == 0){
                        break;
                    }else{
                        location--;
                    }
                }
                // 0번 인덱스 값이 max가 아닌 경우,
                else{
                    // 맨 앞의 요소를 뒤로 보냄
                    ll.add(ll.poll());
                    
                    // location이 0인경우,
                    // 다시 뒤부터 시작
                    // 아닌 경우, 앞으로 당김
                    if(location == 0){
                        location = ll.size()-1;
                    }else{
                        location--;
                    }
                }
            }

            return answer;
        }
}