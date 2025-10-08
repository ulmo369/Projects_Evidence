import java.io.*;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;

public class G {

    public static void main(String[] args) {
        FastReader scan = new FastReader();
        PrintWriter out = new PrintWriter(System.out);
        Task solver = new Task();
        int t = 1;
        for(int tt = 1; tt <= t; tt++) solver.solve(tt, scan, out);
        out.close();
    }

    static class Task {
        static int max = (int) (4e5), MOD = 998244353;
        static long[] fact = new long[max+1], invFact = new long[max+1], naturalInverse = new long[max+1];

        public void solve(int testNumber, FastReader scan, PrintWriter out) {
            int n = scan.nextInt(), k = scan.nextInt();
            Item[] lanterns = new Item[2 * n];
            for(int i = 0; i < n; i++) {
                int l = scan.nextInt(), r = scan.nextInt();
                lanterns[i * 2] = new Item(l, 0);
                lanterns[i * 2 + 1] = new Item(r, 1);
            }
            Arrays.sort(lanterns);
            precomp();

            int have = 0;
            long ans = 0;

            for(Item x : lanterns) {
                if(x.start == 1) have--;
                else {
                    ans = (ans + binomial(have, k - 1)) % MOD;
                    have++;
                }
            }
            out.println(ans);

        }

        static class Item implements Comparable<Item> {
            int val;
            int start;

            public Item(int a, int b) {
                val = a;
                start = b;
            }

            @Override
            public int compareTo(Item item) {
                int ret = Integer.compare(val, item.val);
                if(ret == 0) ret = Integer.compare(start, item.start);
                return ret;
            }
        }


        static void precomp() {
            fact[0] = invFact[0] = invFact[1] = naturalInverse[0] = naturalInverse[1] = 1;
            for(int i = 1; i <= max; i++) {
                fact[i] = (fact[i-1]*i)%MOD;
                if(i == 1) continue;
                naturalInverse[i] = naturalInverse[MOD % i] * (MOD - MOD/i) % MOD;
                invFact[i] = (invFact[i-1]*naturalInverse[i])%MOD;
            }
        }

        static long binomial(int a, int b) {
            if(a < b) return 0;
            return ((fact[a]*invFact[b])%MOD*invFact[a-b])%MOD;
        }


    }

    static void ruffleSort(int[] a) {
        Random get = new Random();
        for (int i = 0; i < a.length; i++) {
            int r = get.nextInt(a.length);
            int temp = a[i];
            a[i] = a[r];
            a[r] = temp;
        }
        Arrays.sort(a);
    }

    static void ruffleSort(long[] a) {
        Random get = new Random();
        for (int i = 0; i < a.length; i++) {
            int r = get.nextInt(a.length);
            long temp = a[i];
            a[i] = a[r];
            a[r] = temp;
        }
        Arrays.sort(a);
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

}