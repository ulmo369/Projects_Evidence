import java.util.*;
import java.io.*;

public class D_1525 {
	
	static int INF = (int)1e9;
	static int n, m;
	static int[] full, free;
	static int[][] memo;
	
	public static int dp(int i, int j) {
		if(i == n)
			return 0;
		if(j == m)
			return INF;
		
		if(memo[i][j] != -1)
			return memo[i][j];
		
		return memo[i][j] = Math.min(dp(i, j + 1), Math.abs(free[j] - full[i]) + dp(i + 1, j + 1));
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		
		int l = sc.nextInt();
		int[] array = sc.nextIntArray(l);
		
		n = 0;
		for(int i = 0; i < l; i++)
			if(array[i] == 1)
				n++;
		m = l - n;
		
		full = new int[n];
		free = new int[m];
		int ind1 = 0, ind2 = 0;
		for(int i = 0; i < l; i++)
			if(array[i] == 0)
				free[ind2++] = i;
			else
				full[ind1++] = i;
		
		memo = new int[n][m];
		for(int[] i : memo)
			Arrays.fill(i, -1);
		
		pw.println(dp(0, 0));
		pw.flush();
	}

	public static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream system) {
			br = new BufferedReader(new InputStreamReader(system));
		}

		public Scanner(String file) throws Exception {
			br = new BufferedReader(new FileReader(file));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public String nextLine() throws IOException {
			return br.readLine();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public char nextChar() throws IOException {
			return next().charAt(0);
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public int[] nextIntArray(int n) throws IOException {
			int[] array = new int[n];
			for (int i = 0; i < n; i++)
				array[i] = nextInt();
			return array;
		}

		public Integer[] nextIntegerArray(int n) throws IOException {
			Integer[] array = new Integer[n];
			for (int i = 0; i < n; i++)
				array[i] = new Integer(nextInt());
			return array;
		}

		public long[] nextLongArray(int n) throws IOException {
			long[] array = new long[n];
			for (int i = 0; i < n; i++)
				array[i] = nextLong();
			return array;
		}

		public double[] nextDoubleArray(int n) throws IOException {
			double[] array = new double[n];
			for (int i = 0; i < n; i++)
				array[i] = nextDouble();
			return array;
		}

		public static int[] shuffle(int[] a) {
			int n = a.length;
			Random rand = new Random();
			for (int i = 0; i < n; i++) {
				int tmpIdx = rand.nextInt(n);
				int tmp = a[i];
				a[i] = a[tmpIdx];
				a[tmpIdx] = tmp;
			}
			return a;
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

		public void waitForInput() throws InterruptedException {
			Thread.sleep(3000);
		}
	}
}
