import java.util.*;
import java.io.*;
public class D {

	public static void main(String[] args) {
		FastScanner sc = new FastScanner();
		int T = sc.nextInt();
		while(T-->0) {
			int n = sc.nextInt();
			int[] arr = new int[n];
			for(int i = 0; i < n; i++) {
				arr[i] = sc.nextInt();
			}
			if(check(arr)) System.out.println("YES");
			else System.out.println("NO");
		}

	}
	static boolean check(int[] arr) {
		int n = arr.length;
		TreeSet<Integer> set = new TreeSet<>();
		set.add(arr[0]);
		for(int i = 1; i < n; i++) {
			set.add(arr[i]);
			if(arr[i-1] == arr[i]) continue;
			Integer x = set.lower(arr[i]);
			if(x != null && x == arr[i-1]) continue;
			x = set.higher(arr[i]);
			if(x != null && x == arr[i-1]) continue;
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
			} catch(IOException e) {
				throw new RuntimeException(e);
			}
		}
	}

}
