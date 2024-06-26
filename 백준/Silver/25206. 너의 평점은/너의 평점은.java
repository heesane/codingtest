// 25206 - 너의 평점은 - 실버 5

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double result = 0;
        double total = 0;

        for (int i = 0; i < 20; i++) {

            double grade = 0;
            double credit = 0;

            String[] strings = br.readLine().split(" ");

            credit += Double.parseDouble(strings[1]);

            switch(strings[2]){
                case "A+":
                    grade += 4.5;
                    break;
                case "A0":
                    grade += 4.0;
                    break;
                case "B+":
                    grade += 3.5;
                    break;
                case "B0":
                    grade += 3.0;
                    break;
                case "C+":
                    grade += 2.5;
                    break;
                case "C0":
                    grade += 2.0;
                    break;
                case "D+":
                    grade += 1.5;
                    break;
                case "D0":
                    grade += 1.0;
                    break;
                case "F":
                    grade += 0.0;
                    break;
                case "P":
                    grade += 0.0;
                    credit = 0;
                    break;
            }
            total += credit;
            result += grade * credit;
        }
        System.out.printf("%.6f", result/total);

    }
}