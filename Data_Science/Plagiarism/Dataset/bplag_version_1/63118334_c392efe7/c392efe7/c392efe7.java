import java.util.*;
import java.io.*;
import java.math.*;

/**
 *
 * @Har_Har_Mahadev
 */

/**
 * Main , Solution , Remove Public
 */
public class D {

	static int visited[];
	static int distance[];
	private static ArrayList<Integer>[] adj;
	 
	
	private static void BFS(int node) {
		
		visited[node] = 1;
		Queue<Integer> q = new LinkedList<Integer>();
		q.offer(node);
		distance[node] = 0;
		
		while(!q.isEmpty()) {
			int curr = q.poll();
			for(int child : adj[curr]) {
				if(visited[child] == 0) {
					q.offer(child);
					distance[child] = distance[curr] + 1;
					visited[child] = 1;
				}
			}
		}
		
	}
	

	public static void process() throws IOException {

		int n = sc.nextInt(),a = sc.nextInt(),b = sc.nextInt(),
				da = sc.nextInt(),db = sc.nextInt();
		adj = new ArrayList[n+1];
		distance = new int[n+1];
		visited = new int[n+1];
		for(int i = 0; i<=n; i++)adj[i] = new ArrayList<Integer>();
		for(int i =1; i<n; i++) {
			int u = sc.nextInt(),v = sc.nextInt();
			adj[u].add(v);
			adj[v].add(u);
		}
		BFS(a);
		if(distance[b] <= da || db-da<=da) {
			System.out.println("Alice");
			return;
		}
		ArrayList<Pair> lis = new ArrayList<D.Pair>();
		for(int i = 1; i<=n; i++)lis.add(new Pair(distance[i], i));
		Collections.sort(lis);
		Pair e = lis.get(n-1);
		distance = new int[n+1];
		visited = new int[n+1];
		BFS(e.y);
		int max = 0;
		for(int i = 1; i<=n; i++)max = max(max,distance[i]);
		if(max-da<=da) {
			System.out.println("Alice");
			return;
		}
		System.out.println("Bob");
	}

	//=============================================================================
	//--------------------------The End---------------------------------
	//=============================================================================
	

	private static void google(int tt) {
		System.out.print("Case #" + (tt) + ": ");
	}

	static FastScanner sc;
	static PrintWriter out;

	public static void main(String[] args) throws IOException {
		boolean oj = true;
		if (oj) {
			sc = new FastScanner();
			out = new PrintWriter(System.out);
		} else {
			sc = new FastScanner(100);
			out = new PrintWriter("output.txt");
		}
		int t = 1;
		t = sc.nextInt();
		int TTT = 1;
		while (t-- > 0) {
			//			google(TTT++);
			process();
		}
		out.flush();
		out.close();
	}

	static class Pair implements Comparable<Pair> {
		int x, y;

		Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public int compareTo(Pair o) {
			return Integer.compare(this.x, o.x);
		}

		//		 @Override
		//		    public boolean equals(Object o) {
		//		        if (this == o) return true;
		//		        if (!(o instanceof Pair)) return false;
		//		        Pair key = (Pair) o;
		//		        return x == key.x && y == key.y;
		//		    }
		//		 
		//		    @Override
		//		    public int hashCode() {
		//		        int result = x;
		//		        result = 31 * result + y;
		//		        return result;
		//		    }
	}

	/////////////////////////////////////////////////////////////////////////////////////////////////////////

	static void debug(Object o) {
		System.out.println(o);
	}

	static void debug(Object x, Object y) {
		System.out.println("(" + x + " , " + y + ")");
	}

	static void println(Object o) {
		out.println(o);
	}

	static void println(int[] o) {
		for (int e : o)
			print(e + " ");
		println();
	}

	static void println(long[] o) {
		for (long e : o)
			print(e + " ");
		println();
	}

	static void println() {
		out.println();
	}

	static void print(Object o) {
		out.print(o);
	}

	static void pflush(Object o) {
		out.println(o);
		out.flush();
	}

	static int ceil(int x, int y) {
		return (x % y == 0 ? x / y : (x / y + 1));
	}

	static long ceil(long x, long y) {
		return (x % y == 0 ? x / y : (x / y + 1));
	}

	static int max(int x, int y) {
		return Math.max(x, y);
	}

	static int min(int x, int y) {
		return Math.min(x, y);
	}

	static int abs(int x) {
		return Math.abs(x);
	}

	static long abs(long x) {
		return Math.abs(x);
	}

	static long sqrt(long z) {
		long sqz = (long) Math.sqrt(z);
		while (sqz * 1L * sqz < z) {
			sqz++;
		}
		while (sqz * 1L * sqz > z) {
			sqz--;
		}
		return sqz;
	}

	static int log2(int N) {
		int result = (int) (Math.log(N) / Math.log(2));
		return result;
	}

	static long max(long x, long y) {
		return Math.max(x, y);
	}

	static long min(long x, long y) {
		return Math.min(x, y);
	}

	public static int gcd(int a, int b) {
		BigInteger b1 = BigInteger.valueOf(a);
		BigInteger b2 = BigInteger.valueOf(b);
		BigInteger gcd = b1.gcd(b2);
		return gcd.intValue();
	}

	public static long gcd(long a, long b) {
		BigInteger b1 = BigInteger.valueOf(a);
		BigInteger b2 = BigInteger.valueOf(b);
		BigInteger gcd = b1.gcd(b2);
		return gcd.longValue();
	}

	public static long lcm(long a, long b) {
		return (a * b) / gcd(a, b);
	}

	public static int lcm(int a, int b) {
		return (a * b) / gcd(a, b);
	}

	public static int lower_bound(int[] arr, int x) {
		int low = 0, high = arr.length, mid = -1;

		while (low < high) {
			mid = (low + high) / 2;

			if (arr[mid] >= x)
				high = mid;
			else
				low = mid + 1;
		}

		return low;
	}

	public static int upper_bound(int[] arr, int x) {
		int low = 0, high = arr.length, mid = -1;

		while (low < high) {
			mid = (low + high) / 2;

			if (arr[mid] > x)
				high = mid;
			else
				low = mid + 1;
		}

		return low;
	}

	/////////////////////////////////////////////////////////////////////////////////////////////////////////

	static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		FastScanner() throws FileNotFoundException {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		FastScanner(int a) throws FileNotFoundException {
			br = new BufferedReader(new FileReader("input.txt"));
		}

		String next() throws IOException {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		String nextLine() throws IOException {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}

		int[] readArray(int n) throws IOException {
			int[] A = new int[n];
			for (int i = 0; i != n; i++) {
				A[i] = sc.nextInt();
			}
			return A;
		}

		long[] readArrayLong(int n) throws IOException {
			long[] A = new long[n];
			for (int i = 0; i != n; i++) {
				A[i] = sc.nextLong();
			}
			return A;
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

	static void reverseArray(int[] a) {
		int n = a.length;
		int arr[] = new int[n];
		for (int i = 0; i < n; i++)
			arr[i] = a[n - i - 1];
		for (int i = 0; i < n; i++)
			a[i] = arr[i];
	}

	static void reverseArray(long[] a) {
		int n = a.length;
		long arr[] = new long[n];
		for (int i = 0; i < n; i++)
			arr[i] = a[n - i - 1];
		for (int i = 0; i < n; i++)
			a[i] = arr[i];
	}

}
