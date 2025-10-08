import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class CF {
	
	private static FS sc = new FS();
	
	private static class FS {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try {
					st=new StringTokenizer(br.readLine());				               
	            } catch (IOException e) {}
			return st.nextToken();
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		long nextLong() {
			return Long.parseLong(next());
		}
	}
	
	private static class extra {
		
		static int[] intArr(int size) {
			int[] a = new int[size];
			for(int i = 0; i < size; i++) a[i] = sc.nextInt();
			return a;
		}
		
		static long[] longArr(int size) {
			long[] a = new long[size];
			for(int i = 0; i < size; i++) a[i] = sc.nextLong();
			return a;
		}
		
		static long intSum(int[] a) {
			long sum = 0; 
			for(int i = 0; i < a.length; i++) {
				sum += a[i];
			}
			return sum;
		}
		
		static long longSum(long[] a) {
			long sum = 0; 
			for(int i = 0; i < a.length; i++) {
				sum += a[i];
			}
			return sum;
		}
		
	}
	
	static long count = 0;
	
	public static void main(String[] args) {
		
		int t = sc.nextInt();
//		int t = 1;
		StringBuilder ret = new StringBuilder();
		while(t-- > 0) {
			int n = sc.nextInt();
			int[] a = extra.intArr(n);
			PriorityQueue<Integer> c = new PriorityQueue<>();
			PriorityQueue<Integer> d = new PriorityQueue<>();
			long sum = 0;
			long min = Long.MAX_VALUE;
			for(int i = 0; i < n; i++) {
				sum += a[i];
				if(i%2 == 0) c.add(a[i]);
				else d.add(a[i]);
				if(i != 0) {
					min = Math.min(min, sum + (n - c.size())*1L*c.peek() + (n-d.size())*1L*d.peek());
				}
			}
			ret.append(min + "\n");
 		}
		System.out.println(ret);
	}
}
