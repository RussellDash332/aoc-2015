import java.util.*;
import java.util.regex.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Pattern pat = Pattern.compile("\\d+");
        Matcher matcher = pat.matcher(sc.nextLine());
        matcher.find();
        int r = Integer.parseInt(matcher.group());
        matcher.find();
        int c = Integer.parseInt(matcher.group());
        long ans = 20151125;
        for (int i = 0; i < (r + c) * (r + c - 1) / 2 - r; i++) {
            ans = 252533 * ans % 33554393;
        }
        System.out.println("Part 1: " + ans);
        System.out.println("Part 2: THE END!");
    }
}