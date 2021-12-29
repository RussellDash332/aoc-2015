import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        List<String[]> cmds = new ArrayList<String[]>();

        while (sc.hasNext()) {
            String line = sc.nextLine();
            String[] tmp = new String[2];
            tmp[0] = line.substring(0, 3);
            tmp[1] = line.substring(4, line.length());
            cmds.add(tmp);
        }

        Map<Character, Long> hm = new HashMap<Character, Long>();
        Map<Character, Long> hm2 = new HashMap<Character, Long>();

        hm.put('a', 0L);
        hm.put('b', 0L);
        hm2.put('a', 1L);
        hm2.put('b', 0L);

        System.out.println("Part 1: " + simulate(hm, cmds));
        System.out.println("Part 2: " + simulate(hm2, cmds));
    }

    static long simulate(Map<Character, Long> hm, List<String[]> cmds) {
        int pos = 0;
        while (pos < cmds.size()) {
            switch (cmds.get(pos)[0]) {
                case "inc":
                    hm.put(cmds.get(pos)[1].charAt(0), hm.get(cmds.get(pos)[1].charAt(0)) + 1);
                    pos++;
                    break;
                case "hlf":
                    hm.put(cmds.get(pos)[1].charAt(0), hm.get(cmds.get(pos)[1].charAt(0)) / 2);
                    pos++;
                    break;
                case "tpl":
                    hm.put(cmds.get(pos)[1].charAt(0), hm.get(cmds.get(pos)[1].charAt(0)) * 3);
                    pos++;
                    break;
                case "jmp":
                    pos += Integer.parseInt(cmds.get(pos)[1]);
                    break;
                case "jio":
                    pos += (hm.get(cmds.get(pos)[1].charAt(0)) == 1) ? Integer.parseInt(cmds.get(pos)[1].substring(3, cmds.get(pos)[1].length())) : 1;
                    break;
                default: // jie
                    pos += (hm.get(cmds.get(pos)[1].charAt(0)) % 2 == 0) ? Integer.parseInt(cmds.get(pos)[1].substring(3, cmds.get(pos)[1].length())) : 1;
                    break;
            }
        }
        return hm.get('b');
    }
}