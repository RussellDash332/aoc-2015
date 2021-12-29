import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int area = 0;
        int ribbon = 0;

        while (sc.hasNext()) {
            String[] line = sc.nextLine().split("x");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);
            int z = Integer.parseInt(line[2]);
            area += 2 * (x * y + y * z + z * x) + Math.min(Math.min(x * y, y * z), z * x);
            ribbon += 2 * (x + y + z - Math.max(Math.max(x, y), z)) + x * y * z;
        }

        System.out.println("Part 1: " + area);
        System.out.println("Part 2: " + ribbon);
    }
}