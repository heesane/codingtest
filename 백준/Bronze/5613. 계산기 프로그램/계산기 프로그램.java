import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int result = Integer.parseInt(sc.nextLine());
        while(sc.hasNextLine()){
            String op = sc.nextLine();
            if(op.equals("=")){
                System.out.println(result);
                break;
            }
            int num = Integer.parseInt(sc.nextLine());
            if(op.equals("+")){
                result += num;
            }else if(op.equals("-")){
                result -= num;
            }else if(op.equals("*")){
                result *= num;
            }else if(op.equals("/")) {
                result /= num;
            }
        }
    }
}
