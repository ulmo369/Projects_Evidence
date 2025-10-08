import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Air {

    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        int T = sc.nextInt();
        for(int tt=0; tt<T;tt++){
        	int n = sc.nextInt(), k=sc.nextInt();
        	int [] positions=new int[k], temp=new int[k];
        	for (int i=0;i<k;i++) positions[i]=sc.nextInt();
        	for (int i=0;i<k;i++) temp[i]=sc.nextInt();
        	int[] forced=new int[n];
        	Arrays.fill(forced, Integer.MAX_VALUE/2);
        	for (int i=0;i<k;i++) forced[positions[i]-1]=temp[i];
        	for (int i=1;i<n;i++) forced[i]=Math.min(forced[i], forced[i-1]+1);
        	for (int i=n-2;i>=0;i--) forced[i]=Math.min(forced[i], forced[i+1]+1);
        	for (int i=0;i<n;i++) System.out.print(forced[i]+" ");
			System.out.println();
		}

    }

    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(String s) {
            try {
                br = new BufferedReader(new FileReader(s));
            } catch (FileNotFoundException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }

        public FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String nextToken() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(nextToken());
        }

        long nextLong() {
            return Long.parseLong(nextToken());
        }

        double nextDouble() {
            return Double.parseDouble(nextToken());
        }
    }
}
