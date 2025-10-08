//package codeforces;	
import java.io.*;
import java.util.*;
public class Solution {
	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
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

		int ni() {
			return Integer.parseInt(next());
		}

		long nl() {
			return Long.parseLong(next());
		}

		double nd() {
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

	
	public static void main(String[] args) throws java.lang.Exception {
		FastReader fr = new FastReader();
		PrintWriter out = new PrintWriter(System.out);
		int t = fr.ni();
		while(t-->0) {
			
			int n = fr.ni();
			long arr [] = new long[n];
			for(int i = 0 ; i < n ; i++) arr[i]= fr.nl();
			long even = arr[0];
			long odd = arr[1];
			long minEven = arr[0];
			long minOdd = arr[1];
			long ans = (minEven*n) + (minOdd*n);
			for(int i = 2 ; i < n ; i++) {
				if((i&1) == 0) {
					even += arr[i];
					minEven = Math.min(minEven, arr[i]);
					long a = (i+2)/2;
					long b = (i+1)-a;
					long temp = (even + (minEven*(n - a)));
					temp += (odd + (minOdd*(n - b)));
					ans = Math.min(ans, temp);
				}else {
					odd += arr[i];
					minOdd = Math.min(minOdd, arr[i]);
					long a = (i+2)/2;
					long b = (i+1)-a;
					long temp = (even + (minEven*(n - a)));
					temp += (odd + (minOdd*(n - b)));
					ans = Math.min(ans, temp);
					
				}
			}
			out.println(ans);
		}
		out.close();
	}
}