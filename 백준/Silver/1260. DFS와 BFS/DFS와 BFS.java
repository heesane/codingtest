import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void bfs(int[][] graph,int start_idx){
        boolean[] visited = new boolean[graph.length];
        Queue<Integer> q = new LinkedList<>();

        visited[start_idx] = true;
        q.add(start_idx);

        while(!q.isEmpty()){
            int cur = q.poll();
            System.out.print(cur+" ");

            for(int i = 0; i< graph[cur].length; i++){
                if(graph[cur][i] == 1 && !visited[i]){
                    q.add(i);
                    visited[i] = true;
                }
            }
        }

    }

    public static void dfs(int[][] graph,int start_idx){

        boolean[] visited = new boolean[graph.length];
        Stack<Integer> s = new Stack<>();
        s.push(start_idx);

        while(!s.isEmpty()){
            int cur = s.pop();
            if (!visited[cur]) {
                System.out.print(cur + " ");
                visited[cur] = true;
                for (int i = graph.length - 1; i >= 1; i--) {  // Reverse order to maintain usual recursive DFS order
                    if (graph[cur][i] == 1 && !visited[i]) {
                        s.push(i);
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N+1][N+1];


        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x][y] = 1;
            graph[y][x] = 1;
        }

        dfs(graph,V);
        System.out.println();
        bfs(graph,V);

    }
}

