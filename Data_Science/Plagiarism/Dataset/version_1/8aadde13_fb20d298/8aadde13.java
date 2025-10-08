import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class A {
    public static void main(String args[]) throws Exception {
        FastScanner sc = new FastScanner();
        int T = 1;
        T = sc.nextInt();
        PrintWriter pw = new PrintWriter(System.out);
        while (T-- > 0) {
            solve(sc, pw);
        }
        pw.close();
    }

    public static void solve(FastScanner sc, PrintWriter pw) throws Exception {
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        if(check(arr)) pw.println("YES");
        else pw.println("NO");
    }

    public static boolean check(int[] arr){
        int n=arr.length;
        TreeSet<Integer> S = new TreeSet<>();
        S.add(arr[0]);
        for(int i=1;i<n;i++) {
            S.add(arr[i]);
            if (arr[i] == arr[i - 1]) continue;
            Integer lb = S.lower(arr[i]);
            if (lb != null && lb == arr[i - 1]) continue;
            Integer ub = S.higher(arr[i]);
            if (ub != null && ub == arr[i - 1]) continue;
            return false;
        }
        return true;
    }

    static class FastScanner {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public FastScanner() {
            reader = new BufferedReader(new InputStreamReader(System.in), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public String nextLine() {
            try {
                return reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }
}