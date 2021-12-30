import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int target = sc.nextInt();
        int n = 1000000;

        int[] presents;
        
        presents = new int[n];
        for (int i = 1; i < n; i++) {
            int tmp = i - 1;
            while (tmp < n) {
                presents[tmp] += 10 * i;
                tmp += i;
            }
            if (presents[i - 1] >= target) {
                System.out.println("Part 1: " + i);
                break;
            }
        }

        presents = new int[n];
        for (int i = 1; i < n; i++) {
            int tmp = i - 1;
            for (int j = 0; j < 50 && tmp < n; j++) {
                presents[tmp] += 11 * i;
                tmp += i;
            }
            if (presents[i - 1] >= target) {
                System.out.println("Part 2: " + i);
                break;
            }
        }
    }
}