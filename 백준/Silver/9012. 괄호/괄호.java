import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

class Main{
    public static void main(String[] args)
            throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());

        String[] str_arr = new String[num];

        Stack<String> stack = new Stack<>();

        for (int i = 0; i < num ; i++) {
            str_arr[i] = br.readLine();
        }

        for(String st : str_arr){

            char[] chars_st = st.toCharArray();

            for(char c : chars_st){
                if( String.valueOf(c).equals("(")){
                    stack.push(String.valueOf(c));
                }
                else{
                    //)인 경우
                    if(stack.isEmpty()){
                        stack.push(String.valueOf(c));
                        break;
                    }
                    else{
                        stack.pop();
                    }
                }

            }
            if(stack.isEmpty()){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }
            stack.clear();
        }
    }
}