import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class D
{
    public static void main(String[] args)
    {
        CP sc =new CP();
        int tt = sc.nextInt();
        while (tt-- > 0) {
            int n = sc.nextInt();
            TreeSet<Long> set = new TreeSet<>();
            long prev = -1;
            boolean flag = true;
            for (int i = 0; i < n; i++) {
                long x = sc.nextInt();
                if (i == 0) {
                    set.add(x);
                    prev = x;
                    continue;
                }
                if (x > prev) {
                    Long high = set.higher(prev);
                    if (high == null) set.add(x);
                    else if (high >= x) set.add(x);
                    else flag = false;
                } else if (x < prev) {
                    Long low = set.lower(prev);
                    if (low == null) set.add(x);
                    else if (low <= x) set.add(x);
                    else flag = false;
                }
                prev = x;
            }
            System.out.println(flag ? "YES" : "NO");
        }
    }
    /*****************************************************************************/
    static class CP
    {
        BufferedReader bufferedReader;
        StringTokenizer stringTokenizer;
        public CP() {
            bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        }
        int nextInt() {
            return Integer.parseInt(NNNN());
        }
        long nextLong() {
            return Long.parseLong(NNNN());
        }
        double nextDouble() {
            return Double.parseDouble(NNNN());
        }
        String NNNN() {
            while (stringTokenizer == null || !stringTokenizer.hasMoreElements()) {
                try {
                    stringTokenizer = new StringTokenizer(bufferedReader.readLine());
                }
                catch (IOException  e) {
                    e.printStackTrace();
                }
            }
            return stringTokenizer.nextToken();
        }
        String nextLine() {
            String spl = "";
            try {
                spl = bufferedReader.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return spl;
        }
    }
    /*****************************************************************************/
}