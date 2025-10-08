import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Codeforces {
    public static void main(String[] args) {
        FastReader fastReader = new FastReader();
        int t = fastReader.nextInt();
        while (t-- > 0) {
            int n = fastReader.nextInt();

            int a[] = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = fastReader.nextInt();
            }
            ArrayList<Integer> b = new ArrayList<>();
            ArrayList<Integer> r = new ArrayList<>();
            char c[] = fastReader.next().toCharArray();
            for (int i = 0; i < n; i++) {
                if (c[i] == 'B') {
                    b.add(a[i]);
                } else {
                    r.add(a[i]);
                }
            }

            Collections.sort(b);
            Collections.sort(r);
            int sizeb = b.size();

            boolean isValid = true;
            for (int i = 1 , j = 0; i <=sizeb; i++ , j++){
                if (b.get(j) <  i){
                    isValid =false;
                }
            }

            for (int i = sizeb+1 , j = 0; i <=n && j < r.size(); i++ , j++){
                if (r.get(j) >  i){
                    isValid =false;
                }
            }

            if (isValid){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }


    }

    static class FastReader {


        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(
                    new InputStreamReader(System.in));
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
